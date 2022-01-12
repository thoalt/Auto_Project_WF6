pytest -v -s tests/MOD/test_RULE_FACTORY_DEVICENAME.py  --junitxml=Test_Result.xml
powershell -nop -c "& {sleep 10}"
python push_result_auto.py