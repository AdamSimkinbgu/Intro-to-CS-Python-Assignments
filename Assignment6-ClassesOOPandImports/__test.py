import unittest
import io
from contextlib import redirect_stdout

class FailedTestException(Exception):
    pass

def fail(msg):
    raise FailedTestException(msg)

class TestSummary(unittest.TestCase):
    def test_init_customer(self):
        from PyBarException import InvalidInputException
        from Customer import Customer
        self.assertRaises(InvalidInputException, Customer, 12, 20, 0.12)
        self.assertRaises(InvalidInputException, Customer, "", 20, 0.12)
        self.assertRaises(InvalidInputException, Customer, "Noa", "20", 0.12)
        self.assertRaises(InvalidInputException, Customer, "Noa", 10, 0.12)
        self.assertRaises(InvalidInputException, Customer, "Noa", 22, "hi")
        self.assertRaises(InvalidInputException, Customer, "Noa", 22, -0.12)
        noa = Customer("Noa", 22, 0.15)
        self.assertEqual("Noa", noa.get_name())
        self.assertEqual(22, noa.get_age())
        self.assertEqual(0.15, noa.tip)

    def test_str_customer(self):
        from Customer import Customer
        noa = Customer("Noa", 22, 0.15)
        self.assertEqual("Name:Noa,Age:22,Tip:15%", str(noa))

    def test_order_table(self):
        from Table import Table
        from PyBarException import EmptyTableException
        from Customer import Customer
        from Group import Group

        menu = {"Macabi": 30, "Negev": 30, "Red Whine": 29, "Salad": 30, "Sandwich": 50}
        table1 = Table(1,2)
        self.assertRaises(EmptyTableException,table1.order,menu)
        table2 = Table(2,4)
        cust1 = Customer("Avi", 22, 0.1)
        cust2 = Customer("Joseph", 27, 0.2)
        group1 = Group([cust1, cust2], {"Macabi": 1, "Negev": 1, "Cake":2})
        table2.seat(group1)
        expected_out1 = "Sorry we don't have Cake.\nYour bill is:\nMacabi..........30\nNegev..........30\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            table2.order(menu)
            self.assertEqual(expected_out1, buf.getvalue())
        table3 = Table(3,3)
        table3.seat(group1)
        expected_out2 = "Sorry we don't have Macabi.\nSorry we don't have Negev.\nSorry we don't have Cake.\nYour " \
                            "bill is:\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            table3.order({})
            self.assertEqual(expected_out2, buf.getvalue())

    def test_shift_get_money_no_permission(self):
        # new workers
        from Manager import Manager
        from Waiter import Waiter
        from Hostess import Hostess
        from Shift import Shift

        tom = Manager("Tom", 25)
        noy = Waiter("Noy", 26)
        essra = Hostess("Essra", 27)
        worker_list = [essra, noy, tom]

        shift = Shift(1,[],[],worker_list,{})
        try:
            shift.get_money(noy)
            fail("Waiter wasn't stopped from withdrawing tips")
        except FailedTestException as e:
            raise e
        except Exception as e:
            self.assertEqual(str(e), "ERROR: Only a manager can access the money")

    def test_access_denied_correct_format(self):
        from PyBarException import AccessDeniedException
        try:
            raise AccessDeniedException("This is a test")
        except AccessDeniedException as e:
            if str(e) not in ["ERROR:This is a test", "ERROR: This is a test"]:
                fail("AccessDeniedException msg isn't general")
        
    def test_large_group_small_table(self):
        from Customer import Customer
        from Group import Group
        from Table import Table
        from PyBarException import TooSmallTableException
        neta = Customer("Neta", 20, 0.12)
        alon = Customer("Alon", 54, 0.2)
        tamar = Customer("Tamar", 30, 0.15)
        yuval = Customer("Yuval", 22, 0.13)

        order = {"Goldstar": 2, "Pina colada": 1, "French fries": 1, "Coke": 1}
        group = Group([neta, alon, tamar, yuval], order)
        table = Table(1, 3)
        try:
            table.seat(group)
            fail("Group bigger than table size was sitted.")
        except TooSmallTableException:
            return
        except FailedTestException as e:
            raise e
        except:
            fail("Wrong exception raised")

    def test_seating_in_taken_table(self):
        from Customer import Customer
        from Group import Group
        from Table import Table
        from PyBarException import OccupiedTableException
        neta = Customer("Neta", 20, 0.12)
        alon = Customer("Alon", 54, 0.2)
        tamar = Customer("Tamar", 30, 0.15)
        yuval = Customer("Yuval", 22, 0.13)
        yoav = Customer("Yoav", 20, 0.1)
        ron = Customer("Ron", 30, 0.2)
        order = {"Goldstar": 2, "Pina colada": 1, "French fries": 1, "Coke": 1}
        group = Group([neta, alon, tamar, yuval], order)

        order1 = {"Goldstar": 3}
        group1 = Group([yoav, ron], order1)

        table = Table(1, 4)
        self.assertEqual(table.is_empty(), True)
        table.seat(group)
        self.assertEqual(table.is_empty(), False)
        try:
            table.seat(group1)
            fail("Group was sitted in a taken table")
        except OccupiedTableException:
            return
        except:
            fail("Wrong exception raised")

    def test_group_smaller(self):
        from Customer import Customer
        from Group import Group
        neta = Customer("Neta", 20, 0.12)
        alon = Customer("Alon", 54, 0.2)
        tamar = Customer("Tamar", 30, 0.15)
        yuval = Customer("Yuval", 22, 0.13)
        yoav = Customer("Yoav", 20, 0.1)
        ron = Customer("Ron", 30, 0.2)
        group = Group([neta, alon, tamar, yuval], dict())
        group1 = Group([yoav, ron], dict())
        self.assertEqual(group < group1, False)
        self.assertEqual(group1 < group, True)
        self.assertEqual(len(group), 4)
        self.assertEqual(len(group1), 2)

    def test_copying_group_order(self):
        from Customer import Customer
        from Group import Group
        from Table import Table
        from PyBarException import OccupiedTableException
        neta = Customer("Neta", 20, 0.12)
        alon = Customer("Alon", 54, 0.2)
        tamar = Customer("Tamar", 30, 0.15)
        yuval = Customer("Yuval", 22, 0.13)
        order = {"Goldstar": 2, "Pina colada": 1, "French fries": 1, "Coke": 1}
        group = Group([neta, alon, tamar, yuval], order)
        order_as_returned = group.get_order()
        self.assertEqual(order, order_as_returned)
        order_as_returned["Goldstar"] = 4
        order_as_returned2 = group.get_order()
        self.assertEqual(order_as_returned2, order)

    def test_correct_table_order_price(self):
        from Customer import Customer
        from Group import Group
        from Table import Table

        # new customers:
        neta = Customer("Neta", 20, 0.12)
        alon = Customer("Alon", 54, 0.2)
        tamar = Customer("Tamar", 30, 0.15)
        yuval = Customer("Yuval", 22, 0.13)

        # new orders
        order = {"Goldstar": 2, "Pina colada": 1, "Pizza": 1}

        # new menu
        menu = {"Goldstar": 35, "Macabi": 32, "Pina colada": 50, "Pizza": 59}

        # new groups
        group = Group([neta, alon, tamar, yuval], order)
        table = Table(1, 4)

        table.seat(group)
        expected_out = ["Goldstar..........70", "Pina colada..........50", "Pizza..........59"]
        with io.StringIO() as buf, redirect_stdout(buf):
            table.order(menu)
            self.assertContains(expected_out, buf.getvalue())

    def test_correct_exception_table_payment(self):
        from Table import Table
        from PyBarException import EmptyTableException
        table = Table(1, 1)
        self.assertRaises(EmptyTableException, table.pay)

    def test_add_money_bad_input(self):
        from Shift import Shift
        from PyBarException import InvalidInputException
        from Manager import Manager
        from Waiter import Waiter
        from Hostess import Hostess

        tom = Manager("Tom", 25)
        noy = Waiter("Noy", 26)
        essra = Hostess("Essra", 27)
        worker_list = [essra, noy, tom]

        shift = Shift(1, [], [], worker_list, {})
        self.assertRaises(InvalidInputException, shift.add_money, -2)

    def test_add_tip_bad_input(self):
        from Shift import Shift
        from PyBarException import InvalidInputException
        from Manager import Manager
        from Waiter import Waiter
        from Hostess import Hostess

        tom = Manager("Tom", 25)
        noy = Waiter("Noy", 26)
        essra = Hostess("Essra", 27)
        worker_list = [essra, noy, tom]

        shift = Shift(1, [], [], worker_list, {})
        self.assertRaises(InvalidInputException, shift.add_tip, -0.2)

    def test_get_tip_not_manager(self):
        from Shift import Shift
        from PyBarException import AccessDeniedException
        from Manager import Manager
        from Waiter import Waiter
        from Hostess import Hostess

        tom = Manager("Tom", 25)
        noy = Waiter("Noy", 26)
        essra = Hostess("Essra", 27)
        worker_list = [essra, noy, tom]

        shift = Shift(1, [], [], worker_list, {})
        self.assertRaises(AccessDeniedException, shift.get_tip, noy)

    def assertPrefix(self, s1, s2):
        # Asserts s1 is a prefix of s2
        if s2.startswith(s1):
            return True
        #print(s2,"#",s1)
        raise FailedTestException(s2,"#",s1)
    
    def assertContains(self, expected_strings, string):
        if all(expected_string in string for expected_string in expected_strings):
            return True
        raise FailedTestException

    
    
if __name__ == '__main__':
    unittest.main()
