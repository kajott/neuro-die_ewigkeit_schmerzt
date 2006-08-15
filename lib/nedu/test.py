
def test(scene):
	import os
	os.system('../player test --scene %s -d -q' % scene)
	raise SystemExit
