# import sys
# sys.path.append('scripts/')
import subprocess
import cleanup_output

def main():
    print("Starting content generation...")
    result = subprocess.run(["python", "morel-generate.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr)

    print("Cleaning up generated files...")
    cleanup_output.delete_generated_files()

    print("Process complete.")

if __name__ == "__main__":
    main()
