import cmd
import os

class TextEditor(cmd.Cmd):
    prompt = "+ "
    intro = "Welcome to the CLI text editor!"
    file_name = None
    text = ""

    def do_open(self, arg):
        """Opens a file for editing."""
        try:
            with open(arg, "r") as f:
                self.text = f.read()
                self.file_name = arg
            print(f"Opened file: {arg}")
        except FileNotFoundError:
            print(f"File not found: {arg}")

    def do_save(self, arg):
        """Saves the content to a file."""
        if not self.file_name:
            print("No file opened.")
            return
        try:
            with open(self.file_name, "w") as f:
                f.write(self.text)
            print(f"Saved file: {self.file_name}")
        except Exception as e:
            print(f"Error saving file: {e}")

    def do_exit(self, arg):
        """Exits the text editor."""
        print("Exiting...")
        return True

    def do_append(self, arg):
        """Appends text to the current content."""
        self.text += arg
        print(f"Appended text: {arg}")

    def do_print(self, arg):
        """Prints the current content."""
        print(self.text)

    def emptyline(self):
        """Pass on empty lines."""
        pass

if __name__ == "__main__":
    TextEditor().cmdloop()
