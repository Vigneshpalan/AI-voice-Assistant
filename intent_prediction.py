import torch
import json
import random
import nltk
from nltk.stem.porter import PorterStemmer
from torch.utils.data import Dataset

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

def load_model(model_file):
    data = torch.load(model_file)
    input_size = data["input_size"]
    output_size = data["output_size"]
    all_words = data["all_words"]
    tags = data["tags"]
    model_state = data["model_state"]

    model = IntentRecognitionModel(input_size, hidden_size=8, output_size=output_size)
    model.load_state_dict(model_state)
    model.eval()

    return model, all_words, tags
def predict_intent_response(query):
    intents_file = "Ai/task.json"
    model_file = "Ai/intent_model.pth"
    hidden_size = 8

    model, all_words, tags = load_model(model_file)

    Stemmer = PorterStemmer()
    words = nltk.word_tokenize(query)
    words = [Stemmer.stem(word.lower()) for word in words]
    bag = [1 if word in words else 0 for word in all_words]

    with torch.no_grad():
        input_tensor = torch.tensor(bag, dtype=torch.float32)
        output = model(input_tensor.unsqueeze(0))
        predicted = torch.argmax(output)
        tag = tags[predicted.item()]

  

    intent_file = intents_file
    with open(intent_file, 'r') as f:
        intents = json.load(f)['intents']
    selected_intent = next((intent for intent in intents if intent['tag'] == tag), None)

    if selected_intent:
        # Retrieve the responses associated with the predicted tag
        responses = selected_intent.get('responses', [])
        
        
        return tag, responses

    return tag, []

if __name__ == "__main__":
    intents_file = "Ai/task.json"
    model_file = "Ai/intent_model.pth"
    hidden_size = 8
