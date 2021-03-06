# -*- coding: utf-8 -*-
from autograd.blocks.hyperbolic import sinh
from autograd.blocks.hyperbolic import cosh
from autograd.blocks.hyperbolic import tanh
from autograd.variable import Variable
import numpy as np
import autograd as ad


def test_sinh_forward():
    ad.set_mode('forward')
# =============================================================================
#   define the input variablet
# =============================================================================
    data=np.random.random(5)
    x=Variable(data)

# =============================================================================
#   define custom block
# =============================================================================
    sinh_block=sinh()

# =============================================================================
#   compute output of custom block
# =============================================================================
    y_block=sinh_block(x)
    y_block.compute_gradients()
# =============================================================================
#   define expected output
# =============================================================================
    data_true=np.sinh(data)
    gradient_true=np.diag(np.cosh(data))

# =============================================================================
#   assert data pass
# =============================================================================
    assert np.equal(data_true, y_block.data).all(), 'wrong sinh data pass. expected {}, given{}'.format(data_true, y_block.data)

# =============================================================================
#   assert gradient forward pass
# =============================================================================
    assert np.equal(gradient_true, y_block.gradient).all(), 'wrong sinh gradient forward pass. expected {}, given{}'.format(gradient_true,y_block.gradient)


def test_sinh_reverse():
    ad.set_mode('reverse')
# =============================================================================
#   define the input variablet
# =============================================================================
    data=np.random.random(5)
    x=Variable(data)

# =============================================================================
#   define custom block
# =============================================================================
    sinh_block=sinh()

# =============================================================================
#   compute output of custom block
# =============================================================================
    y_block=sinh_block(x)
    y_block.compute_gradients()
# =============================================================================
#   define expected output
# =============================================================================
    data_true=np.sinh(data)
    gradient_true=np.diag(np.cosh(data))

# =============================================================================
#   assert data pass
# =============================================================================
    assert np.equal(data_true, y_block.data).all(), 'wrong sinh data pass. expected {}, given{}'.format(data_true, y_block.data)

# =============================================================================
#   assert gradient forward pass
# =============================================================================
    assert np.equal(gradient_true, y_block.gradient).all(), 'wrong sinh gradient forward pass. expected {}, given{}'.format(gradient_true,y_block.gradient)
    ad.set_mode('forward')


def test_cosh_forward():
    ad.set_mode('forward')
# =============================================================================
#   define the input variablet
# =============================================================================
    data=np.random.random(5)
    x=Variable(data)

# =============================================================================
#   define custom block
# =============================================================================
    cosh_block=cosh()

# =============================================================================
#   compute output of custom block
# =============================================================================
    y_block=cosh_block(x)
    y_block.compute_gradients()
# =============================================================================
#   define expected output
# =============================================================================
    data_true=np.cosh(data)
    gradient_true=np.diag(np.sinh(data))

# =============================================================================
#   assert data pass
# =============================================================================
    assert np.equal(data_true, y_block.data).all(), 'wrong cosh data pass. expected {}, given{}'.format(data_true, y_block.data)

# =============================================================================
#   assert gradient forward pass
# =============================================================================
    assert np.equal(gradient_true, y_block.gradient).all(), 'wrong cosh gradient forward pass. expected {}, given{}'.format(gradient_true,y_block.gradient)



def test_cosh_reverse():
    ad.set_mode('reverse')
# =============================================================================
#   define the input variablet
# =============================================================================
    data=np.random.random(5)
    x=Variable(data)

# =============================================================================
#   define custom block
# =============================================================================
    cosh_block=cosh()

# =============================================================================
#   compute output of custom block
# =============================================================================
    y_block=cosh_block(x)
    y_block.compute_gradients()

# =============================================================================
#   define expected output
# =============================================================================
    data_true=np.cosh(data)
    gradient_true=np.diag(np.sinh(data))

# =============================================================================
#   assert data pass
# =============================================================================
    assert np.equal(data_true, y_block.data).all(), 'wrong cosh data pass. expected {}, given{}'.format(data_true, y_block.data)

# =============================================================================
#   assert gradient forward pass
# =============================================================================
    assert np.equal(gradient_true, y_block.gradient).all(), 'wrong cosh gradient forward pass. expected {}, given{}'.format(gradient_true,y_block.gradient)
    ad.set_mode('forward')


def test_tanh_forward():
    ad.set_mode('forward')
# =============================================================================
#   define the input variablet
# =============================================================================
    data=np.random.random(5)
    x = Variable(data)

# =============================================================================
#   define custom block
# =============================================================================
    tanh_block=tanh()

# =============================================================================
#   compute output of custom block
# =============================================================================
    y_block=tanh_block(x)
    y_block.compute_gradients()
# =============================================================================
#   define expected output
# =============================================================================
    data_true=np.tanh(data)
    gradient_true=np.diag(1 - np.tanh(data)**2)

# =============================================================================
#   assert data pass
# =============================================================================
    assert np.equal(data_true, y_block.data).all(), 'wrong tanh data pass. expected {}, given{}'.format(data_true, y_block.data)

# =============================================================================
#   assert gradient forward pass
# =============================================================================
    assert np.equal(gradient_true, y_block.gradient).all(), 'wrong tanh gradient forward pass. expected {}, given{}'.format(gradient_true,y_block.gradient)

def test_tanh_reverse():
    ad.set_mode('reverse')
# =============================================================================
#   define the input variablet
# =============================================================================
    data=np.random.random(5)
    x = Variable(data)

# =============================================================================
#   define custom block
# =============================================================================
    tanh_block=tanh()

# =============================================================================
#   compute output of custom block
# =============================================================================
    y_block=tanh_block(x)
    y_block.compute_gradients()

# =============================================================================
#   define expected output
# =============================================================================
    data_true=np.tanh(data)
    gradient_true=np.diag(1 - np.tanh(data)**2)

# =============================================================================
#   assert data pass
# =============================================================================
    assert np.equal(data_true, y_block.data).all(), 'wrong tanh data pass. expected {}, given{}'.format(data_true, y_block.data)

# =============================================================================
#   assert gradient forward pass
# =============================================================================
    assert np.equal(gradient_true, y_block.gradient).all(), 'wrong tanh gradient forward pass. expected {}, given{}'.format(gradient_true,y_block.gradient)
    ad.set_mode('forward')
