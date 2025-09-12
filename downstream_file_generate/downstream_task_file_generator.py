import pandas as pd
import re
import hashlib, sys

def template_to_regex(template):
    regex = template
    regex = regex.replace("\\", "\\\\")
    regex = regex.replace(".", "\.")
    regex = regex.replace("*", "\*")

    regex = regex.replace("<\*>", ".*")

    regex = regex.replace("(", "\(")
    regex = regex.replace(")", "\)")

    regex = regex.replace("[","\[")
    regex = regex.replace("]","\]")

    regex = regex.replace("|","\|")

    regex = regex.replace("+", "\+")
    regex = regex.replace("?", "\?")
    regex = regex.replace("$", "\$")
    regex = regex.replace("@", "\@")
    regex = regex.replace("^", "\^")

    #regex = regex.replace(":", "\:")
    #regex = regex.replace("\"", "\\\"")

    regex = regex + '$'

    return regex

def generate_logformat_regex(logformat):
    """Function to generate regular expression to split log messages"""
    headers = []
    splitters = re.split(r"(<[^<>]+>)", logformat)
    regex = ""
    for k in range(len(splitters)):
        if k % 2 == 0:
            splitter = re.sub(" +", "\\\s+", splitters[k])
            regex += splitter
        else:
            header = splitters[k].strip("<").strip(">")
            regex += "(?P<%s>.*?)" % header
            headers.append(header)
    regex = re.compile("^" + regex + "$")
    return headers, regex

def log_to_dataframe(log_file, regex, headers, logformat):
    """Function to transform log file to dataframe"""
    log_messages = []
    linecount = 0
    with open(log_file, "r") as fin:
        for line in fin.readlines():
            try:
                match = regex.search(line.strip())
                message = [match.group(header) for header in headers]
                log_messages.append(message)
                linecount += 1
            except Exception as e:
                print("[Warning] Skip line: " + line)
    logdf = pd.DataFrame(log_messages, columns=headers)
    logdf.insert(0, "LineId", None)
    logdf["LineId"] = [i + 1 for i in range(linecount)]
    print("Total lines: ", len(logdf))
    return logdf

Spark_format = '<Date> <Time> <Level> <Component>: <Content>'#Spark log format
Zookeeper_format = '<Date> <Time> - <Level>  \[<Node>:<Component>@<Id>\] - <Content>' #Zookeeper log format
Windows_format = '<Date> <Time>, <Level>                  <Component>    <Content>' #Windows log format
Thunderbird_format = '<Label> <Timestamp> <Date> <User> <Month> <Day> <Time> <Location> <Component>(\[<PID>\])?: <Content>' #Thunderbird_format
Apache_format = '\[<Time>\] \[<Level>\] <Content>' #Apache format
BGL_format = '<Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>' #BGL format
Hadoop_format = '<Date> <Time> <Level> \[<Process>\] <Component>: <Content>' #Hadoop format
HPC_format = '<LogId> <Node> <Component> <State> <Time> <Flag> <Content>' #HPC format
Linux_format = '<Month> <Date> <Time> <Level> <Component>(\[<PID>\])?: <Content>' #Linux format
Mac_format = '<Month>  <Date> <Time> <User> <Component>\[<PID>\]( \(<Address>\))?: <Content>' #Mac format
OpenSSH_format = '<Date> <Day> <Time> <Component> sshd\[<Pid>\]: <Content>' #OpenSSH format
OpenStack_format = '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>' #OpenStack format
HealthApp_format = '<Time>\|<Component>\|<Pid>\|<Content>'
Proxifier_format = '\[<Time>\] <Program> - <Content>'

origin_file = '../data/downstream/data/Zookeeper/Zookeeper.log'
# template_file = '../data/downstream/data/BGL/OpenStack_content_template.csv'
event_file = '../data/downstream/data/Zookeeper/Zookeeper_content_event.csv'
output_file = '../data/downstream/data/Zookeeper/Zookeeper_structured.csv'
headers, regex = generate_logformat_regex(Zookeeper_format)

log_messages = []
linecount = 0
for line in open(origin_file).readlines():
    try:
        match = regex.search(line.strip())
        message = [match.group(header) for header in headers]
        log_messages.append(message)
        linecount += 1
    except Exception as e:
        print("Skip line: " + line)
logdf = pd.DataFrame(log_messages, columns=headers)
logdf.insert(0, "LineId", None)
logdf["LineId"] = [i + 1 for i in range(linecount)]

headers = list(logdf.columns) + ['EventId', 'EventTemplate']
event_df = pd.read_csv(event_file)
output_list = []
log_to_templates = (
    event_df.groupby("Log")["Template"]
    .apply(lambda x: list(dict.fromkeys(x)))
    .to_dict()
)

total = len(logdf)
for index, row in logdf.iterrows():
    percent = (int(index) / total) * 100
    sys.stdout.write(f"\rProcessing: {percent:.2f}%")
    sys.stdout.flush()
    content = row['Content']
    templates = log_to_templates.get(content, [])
    if len(templates) == 1:
        template = templates[0]
        event_id = hashlib.sha256(template.encode()).hexdigest()[:8]
        new_row = row.tolist() + [event_id, template]
        output_list.append(new_row)

output_df = pd.DataFrame(output_list, columns=headers)
output_df.to_csv(output_file, index=False)