# AoB_Parser
This program is meant to aid in the compilation of C and C++ programs into binary patches to be patched onto executables rather than source->executable.
Rather than hardcoding addresses in the source, this parser will run after the preprocessor to find addresses based on byte signatures (AoB) in the target exe, and write those absolute addresses into the source file before the compilation.
