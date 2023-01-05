import unittest
import otp_oops


# from otp import generate_otp
class TestgenerateOTP(unittest.TestCase):

    def testcase1(self):
        size = 4

        #To Check Otp
        res = otp_oops.otp(4)
        self.assertEqual(len(res), size)

        #To Check email address for sender
        Email = otp_oops.emailsender
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        #To Check email address for reciver
        Email2 = otp_oops.emailreceiver
        self.assertIn("@",Email2)
        self.assertIn(".",Email2)
        self.assertIn("com",Email2)



    def testcase2(self):
        size = 4

        # To Check Otp
        res = otp_oops.otp(4)
        self.assertEqual(len(res), size)

        # To Check email address
        Email = otp_oops.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

    def testcase3(self):
        size = 4

        # To Check Otp
        res = otp_oops.otp(4)
        self.assertEqual(len(res), size)

        # To Check email address
        Email = otp_oops.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

        #To Check email address for reciver
        Email2 = otp_oops.emailreceiver
        self.assertIn("@",Email2)
        self.assertIn(".",Email2)
        self.assertIn("com",Email2)

    def testcase4(self):
        size = 4

        # To Check Otp
        res = otp_oops.otp(4)
        self.assertEqual(len(res), size)

        # To Check email address
        Email = otp_oops.emailsender
        self.assertIn("@", Email)
        self.assertIn(".", Email)
        self.assertIn("com", Email)

        #To Check email address for reciver
        Email2 = otp_oops.emailreceiver
        self.assertIn("@",Email2)
        self.assertIn(".",Email2)
        self.assertIn("com",Email2)


if __name__ == '__main__':
    unittest.main()