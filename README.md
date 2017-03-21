# About

Analyze a base64-encoded object

```
[ -d binary_data ] || mkdir binary_data
base64 --decode $hex_file.txt > binary-data/$bin_file.ser
python deserialize.py binary-data/$bin_file.ser
```

Create new object
```
python deserialize.py binary-data/$bin_file.ser -o binary-data/$new_bin_file.ser [-a]
```

Convert back into base64
```
base64 binary-data/$new_bin_file.ser > b64-data/$new_hex_file.txt --wrap=0
```
