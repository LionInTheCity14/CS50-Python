import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()  # cursor can directly talk to db

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos(
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    time TEXT NOT NULL);
               ''')

def list_videos():
    cursor.execute('SELECT * FROM videos;')
    
    print('*' * 100)
    print('-' * 50)
    for row in cursor.fetchall():
        print(f"|  {row[0]}  | {row[1]}  |  {row[2]}  |")
    print('-' * 50)
    print('*' * 100)
    

def add_video(name, time):
    cursor.execute('''
                   INSERT INTO videos(name, time)
                   VALUES(?, ?);
                   ''', (name, time))
    conn.commit()

def update_video(video_id, updated_name, updated_time):
    cursor.execute('''
                   UPDATE videos
                   SET name = ?, time = ?
                   WHERE id = ?
                   ''', (updated_name, updated_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute('''
                   DELETE FROM videos
                   WHERE id = ?
                   ''',(video_id,))
    conn.commit()

def main():
    videos = []
    while True:
        print('\n Youtube manager app with db')
        print('1. List Videos') 
        print('2. Add Video')
        print('3. Update Video')
        print('4. Delete Videos')
        print('5. Exit \n')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input('Enter the video name: ')
                time = input('Enter the duration of the video: ')
                add_video(name, time)
            case '3':
                list_videos()       
                video_id = input('Enter the video ID to update: ')
                updated_name = input('Enter the updated video name: ')
                updated_time = input('Enter the updated duration of the video: ')
                update_video(video_id, updated_name, updated_time)
            case '4':
                list_videos()
                video_id = input('Enter the video ID to delete: ')
                delete_video(video_id)
            case '5':
                break
            case '_':
                print('\n Invalid Choice')
    
    conn.close()    # close the connection after use

if __name__ == '__main__':
    main()
