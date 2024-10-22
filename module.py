import re

def detect_language_with_patterns(code_snippet):
    language_patterns = {
        'HTML': [r'<!DOCTYPE html>', r'<html>', r'<head>', r'<body>', r'<div>', r'<span>', r'<a ', r'</html>', r'<script', r'<style'],
        'CSS': [r'{', r'}', r'color:', r'font-size:', r'background-color:', r'border:', r'margin:', r'padding:', r'\.', r'#'],
        'Python': [r'def ', r'import ', r'print\(', r'class ', r'lambda ', r'__name__', r'elif '],
        'JavaScript': [r'function ', r'console\.log\(', r'var ', r'let ', r'const ', r'=>', r'\$\(', r'document\.getElementById'],
        'TypeScript': [r'function ', r'console\.log\(', r'let ', r'const ', r'import ', r'interface ', r'type ', r'implements '],
        'Java': [r'public class ', r'public static void main', r'System\.out\.println\(', r'import java\.', r'extends ', r'implements '],
        'C': [r'#include <stdio.h>', r'int main\(', r'printf\(', r'#define ', r'#include <stdlib.h>', r'scanf\('],
        'C++': [r'#include <iostream>', r'int main\(', r'std::cout', r'new ', r'delete ', r'std::cin', r'using namespace std;'],
        'Ruby': [r'def ', r'puts ', r'class ', r'end', r'@', r':\w+ =>', r'begin ', r'rescue '],
        'Go': [r'func ', r'package ', r'import ', r'fmt\.Println', r'go ', r'defer ', r'chan ', r'goroutine'],
        'PHP': [r'<\?php', r'echo ', r'array\(', r'->', r'\$_', r'namespace ', r'public function ', r'require '],
        'Swift': [r'func ', r'import ', r'let ', r'var ', r'print\(', r'class ', r'if ', r'swift '],
        'Kotlin': [r'fun ', r'val ', r'var ', r'print\(', r'class ', r'import ', r'when ', r'data class '],
        'R': [r'<-', r'library\(', r'print\(', r'ggplot', r'data\.frame', r'install\.packages\(', r'function\('],
        'Perl': [r'use strict;', r'print "', r'\$[\w]+', r'@[\w]+', r'while\(', r'foreach ', r'next;', r'sub '],
        'Shell': [r'#!/bin/bash', r'echo ', r'ls ', r'cd ', r'if ', r'fi', r'export ', r'while ', r'for ', r'in '],
        'Rust': [r'fn ', r'let mut ', r'extern crate ', r'println!', r'use std::', r'impl ', r'mut ', r'pub struct '],
        'Haskell': [r'module ', r'import ', r'main = ', r'let ', r':: ', r'data ', r'-> ', r'case of '],
        'Scala': [r'object ', r'def ', r'val ', r'var ', r'import ', r'println\(', r'if ', r'yield '],
        'Lua': [r'function ', r'local ', r'print\(', r'end', r'if ', r'then ', r'elseif ', r'else '],
        'Dart': [r'void main\(', r'import ', r'new ', r'class ', r'extends ', r'print\(', r'if ', r'await '],
        'MATLAB': [r'function ', r'end', r'if ', r'elseif ', r'else ', r'for ', r'while ', r'plot\(', r'fprintf\('],
        'VimScript': [r'let ', r'function! ', r'endif', r'call ', r'set ', r'augroup ', r'command! ', r'source '],
        'SQL': [r'SELECT ', r'FROM ', r'WHERE ', r'INSERT INTO ', r'UPDATE ', r'DELETE FROM ', r'JOIN ', r'GROUP BY ', r'ORDER BY '],
    }

    for language in ['HTML', 'CSS']:
        patterns = language_patterns[language]
        if any(re.search(pattern, code_snippet, re.IGNORECASE) for pattern in patterns):
            return language
    
    for language, patterns in language_patterns.items():
        if language not in ['HTML', 'CSS']:  
            if any(re.search(pattern, code_snippet, re.IGNORECASE) for pattern in patterns):
                return language
    
    return "Could not detect the language"


# code_snippet = """
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Test Page</title>
# </head>
# <body>
#     <h1>Hello, World!</h1>
# </body>
# </html>
# """

# detected_language = detect_language_with_patterns(code_snippet)
# print(f"The detected programming language is: {detected_language}")
