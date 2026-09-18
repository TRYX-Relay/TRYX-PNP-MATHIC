from pathlib import Path
import hashlib,json,subprocess,sys

here=Path(__file__).resolve().parent
root=here.parents[1]
subprocess.run([sys.executable, str(root/'submission/check_submission.py')], check=True)
for path,expected in json.loads((here/'SHA256SUMS.json').read_text()).items():
    if hashlib.sha256((root/path).read_bytes()).hexdigest()!=expected:
        raise SystemExit('Hash mismatch: '+path)
for script,receipt in [('replay.py','replay-result.json'),('independent_check.py','independent-result.json')]:
    run=subprocess.run([sys.executable,script],cwd=here,text=True,capture_output=True,check=True)
    if json.loads(run.stdout)!=json.loads((here/receipt).read_text()):
        raise SystemExit('Receipt mismatch: '+script)
print('PASS: source integrity; 17902 formulas; 53706 folds; independent intermediate-state checks; negative control')
