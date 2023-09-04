$exclude = @("venv", "RPAChallange.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "RPAChallange.zip" -Force