# Define variables
$repoPath = "C:\projects\patientriskml"
$commitMessage = "Updated: Improved UI, dropdowns, input validation, and fixed feature alignment in prediction"
$remoteRepo = "https://github.com/nagken/patientriskml.git"

# Navigate to the repository
Write-Host "Navigating to project directory: $repoPath"
Set-Location -Path $repoPath

# Ensure Git is initialized
if (-Not (Test-Path "$repoPath\.git")) {
    Write-Host "Initializing Git repository..."
    git init
}

# Add remote repository (if not already set)
$remoteExists = git remote -v
if ($remoteExists -notmatch $remoteRepo) {
    Write-Host "Adding remote repository..."
    git remote add origin $remoteRepo
}

# Add all changes
Write-Host "Staging all changes..."
git add .

# Commit changes
Write-Host "Committing changes..."
git commit -m "$commitMessage"

# Push changes
Write-Host "Pushing changes to GitHub..."
git push -u origin main

Write-Host "✅ Commit and push completed successfully!"
