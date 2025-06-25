#!/bin/bash
# Script to find and remove large files from Git repository

# Find large files in Git history
echo "Finding large files in Git history..."
git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10 | awk '{print $1}')"

# Remove the artifacts directory from Git tracking (but keep it on disk)
echo "Removing artifacts directory from Git tracking..."
git rm -r --cached spark/artifacts/

# Remove all JAR files from Git tracking (but keep them on disk)
echo "Removing JAR files from Git tracking..."
find . -name "*.jar" | xargs git rm --cached

# Remove ZIP files from Git tracking (but keep them on disk)
echo "Removing ZIP files from Git tracking..."
git rm --cached Files.zip Files\ \(1\).zip

# Amend the last commit if these files were just committed
# git commit --amend -C HEAD

# Or create a new commit
git commit -m "Remove large files from Git tracking"

echo ""
echo "Next steps:"
echo "1. Make sure your .gitignore file includes these patterns:"
echo "   - spark/artifacts/"
echo "   - *.jar"
echo "   - *.zip"
echo ""
echo "2. If the files were committed earlier in history and you want to completely"
echo "   remove them from Git history, you may need to use BFG Repo-Cleaner:"
echo "   https://rtyley.github.io/bfg-repo-cleaner/"
echo ""
echo "3. Example BFG command to remove all files larger than 100MB from history:"
echo "   java -jar bfg.jar --strip-blobs-bigger-than 100M /path/to/your/repo.git"
