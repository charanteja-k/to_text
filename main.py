import os 
import sys
import whisper

def main():
    print('=+'*50)
    print('AUDIO / VIDEO TRANSCRIBING TOOL')
    print('=+'*50)

print('Enter you choice :')
print('1. Audio transcription')
print('2. Video transcription')

choice = input().strip()

if choice not in ['1', '2']:
    print('Invalid Choice\n select only 1 or 2')

file_path = input('Enter the file path : ').strip()

file_path = file_path.strip('/')

if not file_path or not os.path.exists(file_path):
    print(f'File not found at {file_path}')
    sys.exit(1)

if not os.path.isfile(file_path):
    print(f'Error: {file_path} is a directory not a file')
    sys.exit(1)

model = whisper.load_model("base")

try :
    result = model.transcribe(file_path)

except Exception as e:
    print(f'Error during transcription : {e}')
    print('Hint: Ensure FFmpeg is installed on your system.')
    sys.exit(1)
transcription_text = result.get('text','').strip()
print('\n'+'=+'*50)
print(transcription_text)
print('\n'+'=+'*50)


save_option = input('\n Do you want to save the transcription to a file ? (y/n)').strip().lower()
if save_option == 'y' :
    base_name = os.path.splittext(os.path.basename(file_path))[0]
    output_filename = f'{base_name}_transcription.txt'

    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(transcription_text)
            print(f"✅ Saved transcript to: {os.path.abspath(output_filename)}")
    except Exception as e:
        print(f"❌ Failed to save file: {e}")
if __name__ == "__main__":
    main()
