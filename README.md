# One_Func_A_Day

The goal of this project is to show you one function per day. The project leverages the python help() function.
Initial commit prints a random function, but in the future it will be one per day, and the option to be random.

# Usage Example

It will give you a specific function for each day of the month. Unless given the -r random argument. See examples below.

python one_func_a_day.py

```
Help on method_descriptor in str:


str.encode = encode(...)
    S.encode(encoding='utf-8', errors='strict') -> bytes

    Encode S using the codec registered for encoding. Default encoding
    is 'utf-8'. errors may be given to set a different error
    handling scheme. Default is 'strict' meaning that encoding errors raise
    a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
    'xmlcharrefreplace' as well as any other name registered with
    codecs.register_error that can handle UnicodeEncodeErrors.
```

# Arguments -r Random
python one_func_a_day.py -r

```
Help on method_descriptor in str:

str.lower = lower(...)
    S.lower() -> str

    Return a copy of the string S converted to lowercase.
```