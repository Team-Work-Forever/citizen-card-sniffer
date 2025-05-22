#!/bin/bash

cd CCSniff
dotnet publish -c Release --self-contained true /p:PublishSingleFile=true
mv .\\bin\\Release\\net9.0\\win-x64\\publish\\CCSniff.exe ../tools/CCSniff.exe
cd -