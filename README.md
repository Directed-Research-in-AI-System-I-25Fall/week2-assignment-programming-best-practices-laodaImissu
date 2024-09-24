hello world

# Aloha

## What I have learned in this lab

1.**Configure Git**:
  ```bash
  git config --global user.name "My_name"
  git config --global user.email "My_email"
  ``` 

2.**Clone the repository / exchange to the repo**
  ```bash
  git clone https://github.com/username/repo-name.git
  cd repo-name
  ```

3.**Create new file**:
  ```bash
  touch readme.md
  ```

4.**Edit file and commit the change**:
  ```bash
  vim readme.md
  git add readme.md
  git commit -m "......"
  ```

5.**Push changes to remote repo**:
  ```bash
  git push origin main 
  ```

6.**Create a new branch**:
  ```bash
  git checkout -b for_fun
  ```

7.**Switch to the main branch**:
  ```bash
  git checkout main
  ```

8.**Install environment**:
  ```bash
  pip install ......
  ```

9.**Pull branch into main**:
  ```bash
  git merge for_fun
  ```

10.**Reverse changes to step_3**:
  ```bash
  git revert <commit_hash_from_step_3>
  ```


