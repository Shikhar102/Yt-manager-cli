import json

# Load video data from file
def load_data():
    try:
        with open('test.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  

# Save video data to file
def save_data_helper(videos):
    with open('test.txt', 'w') as file:
        json.dump(videos, file)

# List all videos
def list_all_videos(videos):
    if not videos:
        print("No videos found.")
        return
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")

# Add a new video
def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter the video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print("Video added successfully.")

# Update video details
def update_video_details(videos):
    list_all_videos(videos)
    if not videos:
        return
    try:
        index = int(input("Enter the video number to update: ")) - 1
        if 0 <= index < len(videos):
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            videos[index] = {'name': name, 'time': time}
            save_data_helper(videos)
            print("Video details updated successfully.")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Delete a video
def delete_video(videos):
    list_all_videos(videos)
    if not videos:
        return
    try:
        index = int(input("Enter the video number to delete: ")) - 1
        if 0 <= index < len(videos):
            deleted_video = videos.pop(index)
            save_data_helper(videos)
            print(f"Deleted video: {deleted_video['name']}")
        else:
            print("Invalid video number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Main function
def main():
    videos = load_data()
    while True: 
        print("\nYouTube Manager | Choose an option")
        print("1. List all YouTube videos")
        print("2. Add a YouTube video")
        print("3. Update YouTube video details")
        print("4. Delete a YouTube video")
        print("5. Exit the application")
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video_details(videos)
            case "4":
                delete_video(videos)
            case "5":
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
