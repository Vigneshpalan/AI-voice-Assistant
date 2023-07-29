import nltk
from nltk.stem.porter import PorterStemmer
import torch
import numpy as np
import json
from torch.utils.data import Dataset, DataLoader

class IntentDataset(Dataset):
    def __init__(self, intents_file):
        self.intents_file = intents_file
        self.intents = self.load_intents()
        self.all_words, self.tags, self.xy = self.preprocess_intents()

    def load_intents(self):
        with open(self.intents_file, 'r') as f:
            intents = json.load(f)
        return intents

    def preprocess_intents(self):
        Stemmer = PorterStemmer()
        all_words = []
        tags = []
        xy = []

        for intent in self.intents['intents']:
            tag = intent['tag']
            tags.append(tag)

            for pattern in intent['patterns']:
                words = nltk.word_tokenize(pattern)
                words = [Stemmer.stem(word.lower()) for word in words]
                all_words.extend(words)
                xy.append((words, tag))

        ignore_words = [',', '?', '/', '.', '!']
        all_words = sorted(set([word for word in all_words if word not in ignore_words]))
        tags = sorted(set(tags))

        return all_words, tags, xy

    def __len__(self):
        return len(self.xy)

    def __getitem__(self, index):
        pattern, tag = self.xy[index]
        bag = [1 if word in pattern else 0 for word in self.all_words]
        return torch.tensor(bag, dtype=torch.float32), torch.tensor(self.tags.index(tag), dtype=torch.int64)


class IntentRecognitionModel(torch.nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(IntentRecognitionModel, self).__init__()
        self.fc1 = torch.nn.Linear(input_size, hidden_size)
        self.fc2 = torch.nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = torch.relu(self.fc1(x))
        out = self.fc2(out)
        return out

def train_intent_model(intents_file, num_epochs=1000, batch_size=8, learning_rate=0.001, hidden_size=8):
    dataset = IntentDataset(intents_file)
    train_loader = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True, num_workers=0)

    input_size = len(dataset.all_words)
    output_size = len(dataset.tags)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = IntentRecognitionModel(input_size, hidden_size, output_size).to(device)
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for epoch in range(num_epochs):
        for words, labels in train_loader:
            words = words.to(device)
            labels = labels.to(device)
            outputs = model(words)
            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {loss.item():.4f}')

    print(f'Final Loss: {loss.item():.4f}')

    data = {
        "model_state": model.state_dict(),
        "input_size": input_size,
        "output_size": output_size,
        "all_words": dataset.all_words,
        "tags": dataset.tags
    }

    FILE = "Ai\intent_model.pth"
    torch.save(data, FILE)

    print(f"Training Complete, Model Saved To {FILE}")
    print("             ")

if __name__ == "__main__":
    intents_file =r"Ai\task.json"
    train_intent_model(intents_file)
