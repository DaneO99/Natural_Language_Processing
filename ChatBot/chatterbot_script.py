from chatterbot import ChatBot
import time
from chatterbot.trainers import ListTrainer

# Use time.time to replace time.clock which is deprecated
time.clock = time.time

# Create chatbots with SQLite storage adapters
brennanbot = ChatBot("Brennan", storage_adapter="chatterbot.storage.SQLStorageAdapter", database_uri="sqlite:///brennan.sqlite3")
dalebot = ChatBot("Dale", storage_adapter="chatterbot.storage.SQLStorageAdapter", database_uri="sqlite:///dale.sqlite3")

# Initialize trainers for each bot
brennan_trainer = ListTrainer(brennanbot)
dale_trainer = ListTrainer(dalebot)

# Lists to hold training data for each character
dale_train = []
brennan_train = []

# Read and process the script
with open("Processed_Step_Brothers_Script.txt", 'r', encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith("DALE:"):
            dale_train.append(line.split("DALE:")[1].strip())
        elif line.startswith("BRENNAN:"):
            brennan_train.append(line.split("BRENNAN:")[1].strip())

# Train the bots
brennan_trainer.train(brennan_train)
dale_trainer.train(dale_train)

# Define exit conditions
exit_conditions = ("quit", "exit")

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() in exit_conditions:
        break
    else:
        response_brennan = brennanbot.get_response(user_input)
        response_dale = dalebot.get_response(user_input)

        # Determine which character's response to print
        if response_brennan.confidence > response_dale.confidence:
            print(f"BRENNAN: {response_brennan}")
        else:
            print(f"DALE: {response_dale}")
