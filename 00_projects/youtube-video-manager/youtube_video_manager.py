import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n')
    print('*' * 100)
    for idx, video in enumerate(videos, start=1):
        print(f"{idx}. {video['name']}, Duration: {video['time']}")
    print('\n')
    print('*' * 100)


def add_video(videos):
    name = input('Enter video name: ')
    time = input('Enter video time: ')
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    idx_to_update = int(input('Enter the video number to update: '))
    if 1<= idx_to_update <= len(videos):
        name = input('Enter the updated video name: ')
        time = input('Enter the updated time: ')
        videos[idx_to_update - 1] = {'name': name, 'time': time}
        print('\n')
        print('*' * 100)
        print(f"Successfully updated video no: {idx_to_update}")
        print('\n')
        print('*' * 100)
        save_data_helper(videos)
    else:
        print('Invalid video selected')

def delete_video(videos):
    list_all_videos(videos)
    idx_to_deleted = int(input('Enter the video number to delete: '))
    if 1<= idx_to_deleted <= len(videos):  
        del videos[idx_to_deleted - 1]
        print('\n')
        print('*' * 100)
        print(f"Successfully deleted video no: {idx_to_deleted}")
        print('\n')
        print('*' * 100)
        save_data_helper(videos)
    else:
        print('Invalid video selected')

def main():
    videos = load_data()
    while True:
        print('\n Youtube Video Manager\n')
        print('1. List all favourite videos ')
        print('2. Add a youtube video ')
        print('3. Update a youtube video details ')
        print('4. Delete a youtube video ')
        print('5. Exit the application')
        # print(videos)
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print('Invalid choice')

if __name__ == '__main__':
    main()