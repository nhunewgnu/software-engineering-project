# Accessing the AWS Instance

1. Make sure that you have a private key file, obtain the file from the repository by copy and paste into a text file and name that 'unibot.pem'
2. Open your terminal or command prompt.
3. Navigate to the directory containing your "unibot.pem" private key file.
4. Run this command first to ensure that the key is not publicly viewable
```
chmod 400 unibot.pem
```
5. Then run the following command to access your AWS instance via SSH:
```
ssh -i "unibot.pem" ec2-user@ec2-107-20-124-52.compute-1.amazonaws.com
```

# Navigating the Instance

1. After logging in to the instance, you will be in your home directory (`/home/ec2-user`).
2. Use basic Linux commands like `cd`, `ls`, and `mkdir` to navigate and manage directories and files on the instance.
3. There should already be a repository for the project but in case there is not

# Cloning from GitHub

1. First, install Git on your instance if you haven't already:
```
sudo yum install git
```
2. Navigate to the directory where you want to clone your repository.
3. Run the following command to clone the repository, replacing "your-repo-url.git" with the actual URL of your repository:
```
git clone https://github.com/nhunewgnu/software-engineering-project.git
```


# Adding and Committing Files to GitHub

1. Make any necessary changes to your files and save them.
2. Use the following command to stage your changes:

```
git add file1 file2 file3
```

Replace "file1 file2 file3" with the actual names of the files you want to stage. You can also use `git add .` to stage all changes in the repository.

3. Commit your changes with a descriptive message:
```
git commit -m "Your commit message here"
```

4. Finally, push your changes to the remote repository:
```
git push origin main
```
Note: If you have not set up your Git credentials, you might need to configure them using the following commands:

```
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

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

ssh key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQC9SIaDATbcbmCowQep4CYq/PsrJFYYPPOi7jdzEQ5fGjAcycrs7Sr5lC/4XlI4nxKrTFmEdNEV2wjjp32afVcZqSXAOJo+3iIDRXHvw3qocF6RaF3ugzGdMVwi2NDlAZvIgvuZYUDB47OUxkxIxDZl5MmpQeIHycwtrryhhw2o85IauBk+HmX8TKSmFwsimrcbigJibXyggH82mLEr7j1hCEuY+TRhasU+eouQ5vCYTGhck27EqLH1TwsvhtRUxQOVIqDUvkQ6q4ShhoBNqsY/DidAJIF18wNei8ok4sAjjpSACo8lhBU+XbofomSfAJdf2ES3dvGRo/DcVMjDQfTrojuyI6Nh0+lE3KmI4J+przGfzJyBm0KE4Fj3HRYhQ6CDLaGALni9Bz8HGEA693PNGDLSEbPHBrUj6JmNaPJhJcC1Tf2ZBg75roiqQXSI4Wmi7YMG2zQKaa3nhuxqYuEFrDucx1Yf5ke0gszMcUGF+gIp5wW/sfzgbfEezurionR3TU7V4Ra3KFifQfrvVnYRYlPIhi5TVy5jdQo5FnyxAnEnLJLgscAdnZsV09RZtn5Zc6aHGVE3l2bV5+u1kVPd8sQFmAhaa2iRxICAXPgjqQC/yEcaes3EQfRjyxlvqX7ljDss/hnLrGiMXcZQRKL4157zJ8zOmhdVEL0eZyQwCQ== nhunewgnu@gmail.com

