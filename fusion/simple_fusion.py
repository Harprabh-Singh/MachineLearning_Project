# import pandas as pd
# import torch
# from torchvision import datasets, transforms
# from torch.utils.data import DataLoader
# import torch.nn as nn

# # Load ML predictions
# df = pd.read_csv("data/processed/reliance_labeled.csv")

# # ML model (reuse training)
# from sklearn.ensemble import RandomForestClassifier

# feature_columns = [
#     'EMA_DIFF_8_21',
#     'EMA_DIFF_21_50',
#     'EMA_DISTANCE_CLOSE_21',
#     'EMA_SLOPE_21',
#     'EMA_TREND_STRENGTH',
#     'RSI',
#     'RSI_SLOPE',
#     'SMI',
#     'SMI_SLOPE',
#     'PRICE_RANGE'
# ]

# X = df[feature_columns]
# y = df['LABEL']

# split_index = int(len(df) * 0.8)

# X_train = X.iloc[:split_index]
# y_train = y.iloc[:split_index]

# X_test = X.iloc[split_index:]

# model = RandomForestClassifier(
#     n_estimators=100,
#     max_depth=5,
#     class_weight='balanced',
#     random_state=42
# )

# model.fit(X_train, y_train)

# ml_preds = model.predict(X_test)

# # CNN model (same as Phase 10)
# IMAGE_SIZE = 128
# DATA_DIR = "cv/images"

# transform = transforms.Compose([
#     transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
#     transforms.ToTensor()
# ])

# dataset = datasets.ImageFolder(root=DATA_DIR, transform=transform)

# test_size = len(dataset) - int(0.8 * len(dataset))
# _, test_dataset = torch.utils.data.random_split(dataset, [len(dataset)-test_size, test_size])

# test_loader = DataLoader(test_dataset, batch_size=1)

# class SimpleCNN(nn.Module):
#     def __init__(self):
#         super(SimpleCNN, self).__init__()
#         self.conv = nn.Sequential(
#             nn.Conv2d(3, 16, 3, padding=1),
#             nn.ReLU(),
#             nn.MaxPool2d(2),
#             nn.Conv2d(16, 32, 3, padding=1),
#             nn.ReLU(),
#             nn.MaxPool2d(2)
#         )
#         self.fc = nn.Sequential(
#             nn.Flatten(),
#             nn.Linear(32 * 32 * 32, 128),
#             nn.ReLU(),
#             nn.Linear(128, 3)
#         )

#     def forward(self, x):
#         return self.fc(self.conv(x))

# # ⚠️ NOTE: In simple version, we retrain quickly (not loading saved model)
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# cnn_model = SimpleCNN().to(device)

# # Quick training (reuse logic)
# train_dataset, _ = torch.utils.data.random_split(dataset, [int(0.8*len(dataset)), len(dataset)-int(0.8*len(dataset))])
# train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)

# criterion = nn.CrossEntropyLoss()
# optimizer = torch.optim.Adam(cnn_model.parameters(), lr=0.001)

# for epoch in range(3):  # quick training
#     for images, labels in train_loader:
#         images, labels = images.to(device), labels.to(device)
#         optimizer.zero_grad()
#         outputs = cnn_model(images)
#         loss = criterion(outputs, labels)
#         loss.backward()
#         optimizer.step()

# # CNN Predictions
# cnn_preds = []

# cnn_model.eval()
# with torch.no_grad():
#     for images, labels in test_loader:
#         images = images.to(device)
#         outputs = cnn_model(images)
#         _, pred = torch.max(outputs, 1)
#         cnn_preds.append(pred.item())

# # Convert CNN labels → match ML labels
# # ImageFolder mapping: buy=0, hold=1, sell=2
# mapping = {0: 1, 1: 0, 2: -1}
# cnn_preds = [mapping[p] for p in cnn_preds]

# # Fusion Logic
# min_len = min(len(ml_preds), len(cnn_preds))

# final_preds = []

# for i in range(min_len):
#     if ml_preds[i] == cnn_preds[i]:
#         final_preds.append(ml_preds[i])
#     else:
#         final_preds.append(0)  # HOLD

# # Evaluate Fusion
# y_test = y.iloc[split_index:split_index + min_len]

# correct = sum([1 for i in range(min_len) if final_preds[i] == y_test.iloc[i]])
# accuracy = correct / min_len

# print(f"\n📊 FUSION ACCURACY: {accuracy:.2%}")

# # Signal Reduction Insight
# trades_before = sum([1 for x in ml_preds[:min_len] if x != 0])
# trades_after = sum([1 for x in final_preds if x != 0])

# print(f"Trades before fusion: {trades_before}")
# print(f"Trades after fusion: {trades_after}")