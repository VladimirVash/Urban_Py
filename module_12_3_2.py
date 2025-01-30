import unittest
import module_12_3_1

tur_ran_ST = unittest.TestSuite()

tur_ran_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3_1.RunnerTest))
tur_ran_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_3_1.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(tur_ran_ST)