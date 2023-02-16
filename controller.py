import model_init
import model_sum
import model_subtraction
import model_devision
import model_mult
import view
import value
import controller
def button_click():
    value_a = value.get_value()
    value_b = value.get_value()
    model_init.init(value_a, value_b)
    result_sum = model_sum.do_it(value_a, value_b)
    view.view_data(result_sum, 'summation')
    result_sub = model_subtraction.do_it(value_a, value_b)
    view.view_data(result_sub, 'subtraction')
    result_mult = model_mult.do_it(value_a, value_b)
    view.view_data(result_mult, 'multiplication')
    result_dev = model_devision.do_it(value_a, value_b)
    view.view_data(result_dev, 'deviation')


