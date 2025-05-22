Set-Location -Path "CCSniff"

dotnet publish -c Release --self-contained true /p:PublishSingleFile=true

Move-Item -Path ".\bin\Release\net9.0\win-x64\publish\CCSniff.exe" -Destination "..\tools\CCSniff.exe"

Pop-Location