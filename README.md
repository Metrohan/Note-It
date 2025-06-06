# **Note-It**

**Note-It** is a lightweight and straightforward note-taking application designed to help you quickly jot down and save your thoughts. Built with Python and PyQt, this simple app allows users to create, save, open, and edit text-based notes. While it retains an old-fashioned, minimalistic feel, Note-It provides all the essential features you'd expect from a basic note-taking tool, making it ideal for those who prefer simplicity and ease of use.

---

![Screenshot 2023-09-14 234558](https://github.com/Metrohan/Note-It/assets/54481595/b9f1edcc-3a61-4e6b-b5e9-8e2c159a2f54)  ![Screenshot 2023-09-14 234606](https://github.com/Metrohan/Note-It/assets/54481595/5a0ba1d7-8530-4639-9d68-cce11fedc5b1)

---

## **Installation**

### Prerequisites:

To run **Note-It**, you need the following dependencies (if you won't run with exe):

- **Python** (version 3.x or higher)
- **PyQt**: A set of Python bindings for the Qt application framework.

### Installation Steps:

1. Clone the repository or download the source code.
2. Install the required dependencies:

   ```ts
   pip install pyqt5
   ```
### Run the application:
   ```ts
   python note_it.py
   ```

## **Usage Instructions**

1. **Create a New Note:**
   - Open the application and type your note in the text area.

2. **Save the Note:**
   - Click the **'Save'** button to store your note. The content will be saved to a file.

3. **Open a Saved Note:**
   - Click the **'Open'** button to browse and open a previously saved note.

4. **Edit and Delete Notes:**
   - Edit your notes directly within the text area and save them again.
   - To delete a note, simply remove its content and save the file.

---

## **Known Issues**

- **Position Lock:** Unfortunately, you cannot change the position of the application window at this time. If you’re familiar with PyQt, feel free to contribute by submitting a pull request.

---

## **Todo**

- Enable the ability to move the application window.
- Implement features for better note organization (e.g., folders, tags).
- Add support for rich text formatting (e.g., bold, italic, bullet points).
- Enhance the user interface for a more modern look and feel.

---

## **Contributing**

Contributions are welcome! If you'd like to improve **Note-It**, feel free to fork the repository and submit pull requests. Whether it’s fixing a bug or adding new features, your help is appreciated.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
