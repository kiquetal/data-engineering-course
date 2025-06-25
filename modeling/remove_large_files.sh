#!/bin/bash
# Script to find and remove large files from Git repository

echo "======================= LARGE FILE REMOVAL SCRIPT ========================"
echo "This script will help remove large files that exceed GitHub's 100MB limit"
echo "========================================================================"

# Find large files in Git history
echo "Finding large files in Git history..."
git rev-list --objects --all | grep "$(git verify-pack -v .git/objects/pack/*.idx | sort -k 3 -n | tail -10 | awk '{print $1}')"

# List all files larger than 50MB
echo "Finding all files larger than 50MB..."
find . -type f -size +50M | grep -v ".git/" | sort -h

# Determine the correct paths based on execution location
ROOT_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo "$(pwd)")"
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
CURRENT_DIR="$(pwd)"

echo "Script is running from: $CURRENT_DIR"
echo "Script is located at: $SCRIPT_DIR"
echo "Git repository root is: $ROOT_DIR"

# Specifically remove the problematic Files.zip
echo "Removing Files.zip from Git tracking (but keeping it on disk)..."
git rm --cached "Files.zip" 2>/dev/null || echo "Files.zip not found in Git index"
git rm --cached "Files (1).zip" 2>/dev/null || echo "Files (1).zip not found in Git index"
git rm --cached "Files_modeling.zip" 2>/dev/null || echo "Files_modeling.zip not found in Git index"

# Remove the artifacts directory from Git tracking (but keep it on disk)
echo "Removing artifacts directory from Git tracking..."
git rm -r --cached modeling/spark/artifacts/ 2>/dev/null || echo "No artifacts directory in Git index"

# Remove all JAR files from Git tracking (but keep them on disk)
echo "Removing JAR files from Git tracking..."
git ls-files "*.jar" | xargs -r git rm --cached 2>/dev/null || echo "No JAR files in Git index"

# Remove all ZIP files from Git tracking (but keep them on disk)
echo "Removing all ZIP files from Git tracking..."
git ls-files "*.zip" | xargs -r git rm --cached 2>/dev/null || echo "No ZIP files in Git index"

# Create or update .gitignore - use the repository root directory
echo "Creating/updating .gitignore file..."
GITIGNORE_FILE="$ROOT_DIR/.gitignore"

if [ -f "$GITIGNORE_FILE" ]; then
    # Check if patterns already exist, add them if not
    grep -q "modeling/spark/artifacts/" "$GITIGNORE_FILE" || echo "modeling/spark/artifacts/" >> "$GITIGNORE_FILE"
    grep -q "spark/artifacts/" "$GITIGNORE_FILE" || echo "spark/artifacts/" >> "$GITIGNORE_FILE"
    grep -q "*.jar" "$GITIGNORE_FILE" || echo "*.jar" >> "$GITIGNORE_FILE"
    grep -q "*.zip" "$GITIGNORE_FILE" || echo "*.zip" >> "$GITIGNORE_FILE"
    grep -q "pyspark_env/" "$GITIGNORE_FILE" || echo "pyspark_env/" >> "$GITIGNORE_FILE"
    grep -q "modeling/spark/pyspark_env/" "$GITIGNORE_FILE" || echo "modeling/spark/pyspark_env/" >> "$GITIGNORE_FILE"
    grep -q "Files.zip" "$GITIGNORE_FILE" || echo "Files.zip" >> "$GITIGNORE_FILE"
    grep -q "Files (1).zip" "$GITIGNORE_FILE" || echo "Files (1).zip" >> "$GITIGNORE_FILE"
    grep -q "Files_modeling.zip" "$GITIGNORE_FILE" || echo "Files_modeling.zip" >> "$GITIGNORE_FILE"
else
    # Create new .gitignore file
    cat > "$GITIGNORE_FILE" << EOL
# Large files and directories
spark/artifacts/
modeling/spark/artifacts/
pyspark_env/
modeling/spark/pyspark_env/
*.jar
*.zip

# Specifically exclude these large files
Files.zip
Files (1).zip
Files_modeling.zip
EOL
fi

# Stage the .gitignore file changes
echo "Staging .gitignore changes..."
git add "$GITIGNORE_FILE"

# Stage the removals (in case they haven't been automatically staged)
git add -u

# Create a commit with the changes
echo "Committing changes..."
git commit -m "Remove large files from Git tracking" || echo "No changes to commit"

echo ""
echo "============= NEXT STEPS ==============="
echo "1. Your .gitignore file has been updated to exclude large files"
echo "2. Large files have been removed from Git tracking (but kept on disk)"
echo "3. You should now be able to push to GitHub without the file size error"
echo ""
echo "If you still have issues with file size limits when pushing, it may be"
echo "because the large files are still in your Git history. To completely"
echo "remove them from history, you can use:"
echo ""
echo "git filter-branch --force --index-filter \\"
echo "  'git rm --cached --ignore-unmatch Files.zip' \\"
echo "  --prune-empty --tag-name-filter cat -- --all"
echo ""
echo "Or use the BFG Repo-Cleaner tool: https://rtyley.github.io/bfg-repo-cleaner/"
