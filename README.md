# 🎥 YouTube Video Manager

A simple, lightweight CLI-based video management system using Python and JSON for data storage. Manage your YouTube videos with ease—add, update, delete, and list videos right from your terminal.

---

## 📖 Features
- 📄 **List Videos**: View all saved YouTube videos.
- ➕ **Add Videos**: Add new videos with name and duration.
- ✏️ **Update Videos**: Modify video details interactively.
- ❌ **Delete Videos**: Remove videos by selecting from a list.
- 💾 **Persistent Storage**: Saves data using JSON files.

---

## 📂 Project Structure
```plaintext
├── test.txt              # JSON file for storing video data
├── video_manager.py      # Main script file
├── README.md             # Documentation file
```

---

# 🚀 How to Install and Run

## 1️⃣ Fork the Repositor
- Navigate to the YouTube Video Manager GitHub repo.
- Click the Fork button at the top-right corner of the page.

## 2️⃣ Clone the Repository

```bash
https://github.com/Shikhar102/Yt-manager-cli.git
``` 
## 3️⃣ Navigate to the Directory

```bash
cd youtube_manager.py
```
## 4️⃣ Install Dependencies
- No external dependencies required.
- Ensure Python 3.7+ is installed on your system.

# 📋 Code Snippets

## Adding a Video
```python
def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video added successfully.")
```

## Listing All Videos
```python
def list_all_videos(videos):
    if not videos:
        print("No videos found.")
        return
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
```
# 💻 Usage

- Choose an option from the menu:
    1. to list videos.
    2. to add a video.
    3. to update video details.
    4. to delete a video.
    5. to exit the application.

- Follow the prompts to manage your videos effectively.

## 🛠️ Contributing

We welcome contributions to improve this project. Follow the steps below:

### 1. Fork the project:
```bash
git fork https://github.com/Shikhar102/Yt-manager-cli.git
```

### 2. Create your feature branch:
```bash
git checkout -b feature/AmazingFeature
```

### 3. Commit your changes:
```bash
git commit -m "Add some AmazingFeature"
```

### 4. Push to the branch:
```bash
git push origin feature/AmazingFeature
```

### 5. Open a pull request on GitHub.

# 📜 License
- This project is licensed under the MIT License. Feel free to use and modify the code.




