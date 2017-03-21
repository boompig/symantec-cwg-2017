# About

How to run

```
[ -d binary_data ] || mkdir binary_data
base64 --decode $hex_file > binary_data/$bin_file.ser
python deserialize binary_data/$bin_file.ser
```

