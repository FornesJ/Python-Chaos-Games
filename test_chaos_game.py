from chaos_game import ChaosGame
import pytest

@pytest.mark.parametrize("n, r", [(2, 2)])
def test_ChaosGame_constructor(n, r):
	# testing if n = 2 raisas ValueError
	try:
		ChaosGame(n, 0.5)
	except ValueError:
		assert True

	# testing if r = 2 raisas ValueError
	try:
		ChaosGame(3, r)
	except ValueError:
		assert True

def test_savepng(outfile="testfile.jpeg"):
	CG = ChaosGame(3, 0.5)
	CG.iterate(1000)
	try:
		CG.savepng(outfile)
	except ValueError:
		assert True



		
