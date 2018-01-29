# This file was automatically created by FeynRules 2.0.33
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Fri 24 Jul 2015 10:44:58



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\text{aS}',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.0025499999999999997,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.0005110000000000001,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MN = Parameter(name = 'MN',
               nature = 'external',
               type = 'real',
               value = 200,
               texname = '\\text{MN}',
               lhablock = 'FRBlock',
               lhacode = [ 1 ])

WN = Parameter(name = 'WN',
               nature = 'external',
               type = 'real',
               value = 0.0001,
               texname = '\\text{WN}',
               lhablock = 'FRBlock',
               lhacode = [ 2 ])

yvN1 = Parameter(name = 'yvN1',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\text{yvN1}',
                 lhablock = 'FRBlock',
                 lhacode = [ 3 ])

yvN2 = Parameter(name = 'yvN2',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\text{yvN2}',
                 lhablock = 'FRBlock',
                 lhacode = [ 4 ])

yvN3 = Parameter(name = 'yvN3',
                 nature = 'external',
                 type = 'real',
                 value = 0.1,
                 texname = '\\text{yvN3}',
                 lhablock = 'FRBlock',
                 lhacode = [ 5 ])

MN1 = Parameter(name = 'MN1',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = '\\text{MN1}',
                lhablock = 'MASS',
                lhacode = [ 1000022 ])

MN2 = Parameter(name = 'MN2',
                nature = 'external',
                type = 'real',
                value = 200,
                texname = '\\text{MN2}',
                lhablock = 'MASS',
                lhacode = [ 1000023 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.0005110000000000001,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MM = Parameter(name = 'MM',
               nature = 'external',
               type = 'real',
               value = 0.10566,
               texname = '\\text{MM}',
               lhablock = 'MASS',
               lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.0025499999999999997,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.42,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WN1 = Parameter(name = 'WN1',
                nature = 'external',
                type = 'real',
                value = 0.0001,
                texname = '\\text{WN1}',
                lhablock = 'DECAY',
                lhacode = [ 1000022 ])

WN2 = Parameter(name = 'WN2',
                nature = 'external',
                type = 'real',
                value = 0.0001,
                texname = '\\text{WN2}',
                lhablock = 'DECAY',
                lhacode = [ 1000023 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\text{aEW}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

theta1 = Parameter(name = 'theta1',
                   nature = 'internal',
                   type = 'real',
                   value = '(174.10383166375172*yvN1)/MN',
                   texname = '\\text{theta1}')

theta2 = Parameter(name = 'theta2',
                   nature = 'internal',
                   type = 'real',
                   value = '(174.10383166375172*yvN2)/MN',
                   texname = '\\text{theta2}')

theta3 = Parameter(name = 'theta3',
                   nature = 'internal',
                   type = 'real',
                   value = '(174.10383166375172*yvN3)/MN',
                   texname = '\\text{theta3}')

tvN2 = Parameter(name = 'tvN2',
                 nature = 'internal',
                 type = 'real',
                 value = '(30312.1442*(yvN1**2 + yvN2**2 + yvN3**2))/MN**2',
                 texname = '\\theta ^2')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

Uv4x1 = Parameter(name = 'Uv4x1',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{Uv4x1}')

Uv4x2 = Parameter(name = 'Uv4x2',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{Uv4x2}')

Uv4x3 = Parameter(name = 'Uv4x3',
                  nature = 'internal',
                  type = 'complex',
                  value = '0',
                  texname = '\\text{Uv4x3}')

Uv4x4 = Parameter(name = 'Uv4x4',
                  nature = 'internal',
                  type = 'complex',
                  value = 'complex(0,1)/cmath.sqrt(2)',
                  texname = '\\text{Uv4x4}')

Uv4x5 = Parameter(name = 'Uv4x5',
                  nature = 'internal',
                  type = 'complex',
                  value = '1/cmath.sqrt(2)',
                  texname = '\\text{Uv4x5}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = '80.357*(1 + 0.11*(theta1**2 + theta2**2))',
               texname = 'M_W')

PMNS1x1 = Parameter(name = 'PMNS1x1',
                    nature = 'internal',
                    type = 'real',
                    value = '1 - theta1**2/2.',
                    texname = '\\text{PMNS1x1}')

PMNS1x2 = Parameter(name = 'PMNS1x2',
                    nature = 'internal',
                    type = 'real',
                    value = '-(theta1*theta2)/2.',
                    texname = '\\text{PMNS1x2}')

PMNS1x3 = Parameter(name = 'PMNS1x3',
                    nature = 'internal',
                    type = 'real',
                    value = '-(theta1*theta3)/2.',
                    texname = '\\text{PMNS1x3}')

PMNS2x1 = Parameter(name = 'PMNS2x1',
                    nature = 'internal',
                    type = 'real',
                    value = '-(theta1*theta2)/2.',
                    texname = '\\text{PMNS2x1}')

PMNS2x2 = Parameter(name = 'PMNS2x2',
                    nature = 'internal',
                    type = 'real',
                    value = '1 - theta2**2/2.',
                    texname = '\\text{PMNS2x2}')

PMNS2x3 = Parameter(name = 'PMNS2x3',
                    nature = 'internal',
                    type = 'real',
                    value = '-(theta2*theta3)/2.',
                    texname = '\\text{PMNS2x3}')

PMNS3x1 = Parameter(name = 'PMNS3x1',
                    nature = 'internal',
                    type = 'real',
                    value = '-(theta1*theta3)/2.',
                    texname = '\\text{PMNS3x1}')

PMNS3x2 = Parameter(name = 'PMNS3x2',
                    nature = 'internal',
                    type = 'real',
                    value = '-(theta2*theta3)/2.',
                    texname = '\\text{PMNS3x2}')

PMNS3x3 = Parameter(name = 'PMNS3x3',
                    nature = 'internal',
                    type = 'real',
                    value = '1 - theta3**2/2.',
                    texname = '\\text{PMNS3x3}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '0.2315*(1 - 0.71*(theta1**2 + theta2**2))',
                texname = '\\text{sw2}')

Theta4x4 = Parameter(name = 'Theta4x4',
                     nature = 'internal',
                     type = 'complex',
                     value = 'tvN2/2.',
                     texname = '\\text{Theta4x4}')

Theta4x5 = Parameter(name = 'Theta4x5',
                     nature = 'internal',
                     type = 'complex',
                     value = '(complex(0,1)*tvN2)/2.',
                     texname = '\\text{Theta4x5}')

Theta5x4 = Parameter(name = 'Theta5x4',
                     nature = 'internal',
                     type = 'complex',
                     value = '-(complex(0,1)*tvN2)/2.',
                     texname = '\\text{Theta5x4}')

Theta5x5 = Parameter(name = 'Theta5x5',
                     nature = 'internal',
                     type = 'complex',
                     value = 'tvN2/2.',
                     texname = '\\text{Theta5x5}')

Uv1x4 = Parameter(name = 'Uv1x4',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((complex(0,1)*theta1)/cmath.sqrt(2))',
                  texname = '\\text{Uv1x4}')

Uv1x5 = Parameter(name = 'Uv1x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'theta1/cmath.sqrt(2)',
                  texname = '\\text{Uv1x5}')

Uv2x4 = Parameter(name = 'Uv2x4',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((complex(0,1)*theta2)/cmath.sqrt(2))',
                  texname = '\\text{Uv2x4}')

Uv2x5 = Parameter(name = 'Uv2x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'theta2/cmath.sqrt(2)',
                  texname = '\\text{Uv2x5}')

Uv3x4 = Parameter(name = 'Uv3x4',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((complex(0,1)*theta3)/cmath.sqrt(2))',
                  texname = '\\text{Uv3x4}')

Uv3x5 = Parameter(name = 'Uv3x5',
                  nature = 'internal',
                  type = 'complex',
                  value = 'theta3/cmath.sqrt(2)',
                  texname = '\\text{Uv3x5}')

Uv5x1 = Parameter(name = 'Uv5x1',
                  nature = 'internal',
                  type = 'complex',
                  value = '-theta1',
                  texname = '\\text{Uv5x1}')

Uv5x2 = Parameter(name = 'Uv5x2',
                  nature = 'internal',
                  type = 'complex',
                  value = '-theta2',
                  texname = '\\text{Uv5x2}')

Uv5x3 = Parameter(name = 'Uv5x3',
                  nature = 'internal',
                  type = 'complex',
                  value = '-theta3',
                  texname = '\\text{Uv5x3}')

Uv5x4 = Parameter(name = 'Uv5x4',
                  nature = 'internal',
                  type = 'complex',
                  value = '-((complex(0,1)*(1 + (-theta1**2 - theta2**2 - theta3**2)/2.))/cmath.sqrt(2))',
                  texname = '\\text{Uv5x4}')

Uv5x5 = Parameter(name = 'Uv5x5',
                  nature = 'internal',
                  type = 'complex',
                  value = '(1 + (-theta1**2 - theta2**2 - theta3**2)/2.)/cmath.sqrt(2)',
                  texname = '\\text{Uv5x5}')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

Theta1x1 = Parameter(name = 'Theta1x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNS1x1**2 + PMNS2x1**2 + PMNS3x1**2',
                     texname = '\\text{Theta1x1}')

Theta1x2 = Parameter(name = 'Theta1x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNS1x1*PMNS1x2 + PMNS2x1*PMNS2x2 + PMNS3x1*PMNS3x2',
                     texname = '\\text{Theta1x2}')

Theta1x3 = Parameter(name = 'Theta1x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNS1x1*PMNS1x3 + PMNS2x1*PMNS2x3 + PMNS3x1*PMNS3x3',
                     texname = '\\text{Theta1x3}')

Theta1x4 = Parameter(name = 'Theta1x4',
                     nature = 'internal',
                     type = 'complex',
                     value = '-((complex(0,1)*(PMNS1x1*theta1 + PMNS1x2*theta2 + PMNS1x3*theta3))/cmath.sqrt(2))',
                     texname = '\\text{Theta1x4}')

Theta1x5 = Parameter(name = 'Theta1x5',
                     nature = 'internal',
                     type = 'complex',
                     value = '(PMNS1x1*theta1 + PMNS1x2*theta2 + PMNS1x3*theta3)/cmath.sqrt(2)',
                     texname = '\\text{Theta1x5}')

Theta2x1 = Parameter(name = 'Theta2x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNS1x1*PMNS1x2 + PMNS2x1*PMNS2x2 + PMNS3x1*PMNS3x2',
                     texname = '\\text{Theta2x1}')

Theta2x2 = Parameter(name = 'Theta2x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNS1x2**2 + PMNS2x2**2 + PMNS3x2**2',
                     texname = '\\text{Theta2x2}')

Theta2x3 = Parameter(name = 'Theta2x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNS1x2*PMNS1x3 + PMNS2x2*PMNS2x3 + PMNS3x2*PMNS3x3',
                     texname = '\\text{Theta2x3}')

Theta2x4 = Parameter(name = 'Theta2x4',
                     nature = 'internal',
                     type = 'complex',
                     value = '-((complex(0,1)*(PMNS2x1*theta1 + PMNS2x2*theta2 + PMNS2x3*theta3))/cmath.sqrt(2))',
                     texname = '\\text{Theta2x4}')

Theta2x5 = Parameter(name = 'Theta2x5',
                     nature = 'internal',
                     type = 'complex',
                     value = '(PMNS2x1*theta1 + PMNS2x2*theta2 + PMNS2x3*theta3)/cmath.sqrt(2)',
                     texname = '\\text{Theta2x5}')

Theta3x1 = Parameter(name = 'Theta3x1',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNS1x1*PMNS1x3 + PMNS2x1*PMNS2x3 + PMNS3x1*PMNS3x3',
                     texname = '\\text{Theta3x1}')

Theta3x2 = Parameter(name = 'Theta3x2',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNS1x2*PMNS1x3 + PMNS2x2*PMNS2x3 + PMNS3x2*PMNS3x3',
                     texname = '\\text{Theta3x2}')

Theta3x3 = Parameter(name = 'Theta3x3',
                     nature = 'internal',
                     type = 'complex',
                     value = 'PMNS1x3**2 + PMNS2x3**2 + PMNS3x3**2',
                     texname = '\\text{Theta3x3}')

Theta3x4 = Parameter(name = 'Theta3x4',
                     nature = 'internal',
                     type = 'complex',
                     value = '-((complex(0,1)*(PMNS3x1*theta1 + PMNS3x2*theta2 + PMNS3x3*theta3))/cmath.sqrt(2))',
                     texname = '\\text{Theta3x4}')

Theta3x5 = Parameter(name = 'Theta3x5',
                     nature = 'internal',
                     type = 'complex',
                     value = '(PMNS3x1*theta1 + PMNS3x2*theta2 + PMNS3x3*theta3)/cmath.sqrt(2)',
                     texname = '\\text{Theta3x5}')

Theta4x1 = Parameter(name = 'Theta4x1',
                     nature = 'internal',
                     type = 'complex',
                     value = '(complex(0,1)*(PMNS1x1*theta1 + PMNS2x1*theta2 + PMNS3x1*theta3))/cmath.sqrt(2)',
                     texname = '\\text{Theta4x1}')

Theta4x2 = Parameter(name = 'Theta4x2',
                     nature = 'internal',
                     type = 'complex',
                     value = '(complex(0,1)*(PMNS1x2*theta1 + PMNS2x2*theta2 + PMNS3x2*theta3))/cmath.sqrt(2)',
                     texname = '\\text{Theta4x2}')

Theta4x3 = Parameter(name = 'Theta4x3',
                     nature = 'internal',
                     type = 'complex',
                     value = '(complex(0,1)*(PMNS1x3*theta1 + PMNS2x3*theta2 + PMNS3x3*theta3))/cmath.sqrt(2)',
                     texname = '\\text{Theta4x3}')

Theta5x1 = Parameter(name = 'Theta5x1',
                     nature = 'internal',
                     type = 'complex',
                     value = '(PMNS1x1*theta1 + PMNS2x1*theta2 + PMNS3x1*theta3)/cmath.sqrt(2)',
                     texname = '\\text{Theta5x1}')

Theta5x2 = Parameter(name = 'Theta5x2',
                     nature = 'internal',
                     type = 'complex',
                     value = '(PMNS1x2*theta1 + PMNS2x2*theta2 + PMNS3x2*theta3)/cmath.sqrt(2)',
                     texname = '\\text{Theta5x2}')

Theta5x3 = Parameter(name = 'Theta5x3',
                     nature = 'internal',
                     type = 'complex',
                     value = '(PMNS1x3*theta1 + PMNS2x3*theta2 + PMNS3x3*theta3)/cmath.sqrt(2)',
                     texname = '\\text{Theta5x3}')

Uv1x1 = Parameter(name = 'Uv1x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x1',
                  texname = '\\text{Uv1x1}')

Uv1x2 = Parameter(name = 'Uv1x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x2',
                  texname = '\\text{Uv1x2}')

Uv1x3 = Parameter(name = 'Uv1x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS1x3',
                  texname = '\\text{Uv1x3}')

Uv2x1 = Parameter(name = 'Uv2x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS2x1',
                  texname = '\\text{Uv2x1}')

Uv2x2 = Parameter(name = 'Uv2x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS2x2',
                  texname = '\\text{Uv2x2}')

Uv2x3 = Parameter(name = 'Uv2x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS2x3',
                  texname = '\\text{Uv2x3}')

Uv3x1 = Parameter(name = 'Uv3x1',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS3x1',
                  texname = '\\text{Uv3x1}')

Uv3x2 = Parameter(name = 'Uv3x2',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS3x2',
                  texname = '\\text{Uv3x2}')

Uv3x3 = Parameter(name = 'Uv3x3',
                  nature = 'internal',
                  type = 'complex',
                  value = 'PMNS3x3',
                  texname = '\\text{Uv3x3}')

UvCL1x4 = Parameter(name = 'UvCL1x4',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv1x4',
                    texname = '\\text{UvCL1x4}')

UvCL1x5 = Parameter(name = 'UvCL1x5',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv1x5',
                    texname = '\\text{UvCL1x5}')

UvCL2x4 = Parameter(name = 'UvCL2x4',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv2x4',
                    texname = '\\text{UvCL2x4}')

UvCL2x5 = Parameter(name = 'UvCL2x5',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv2x5',
                    texname = '\\text{UvCL2x5}')

UvCL3x4 = Parameter(name = 'UvCL3x4',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv3x4',
                    texname = '\\text{UvCL3x4}')

UvCL3x5 = Parameter(name = 'UvCL3x5',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv3x5',
                    texname = '\\text{UvCL3x5}')

UvCLdagger4x1 = Parameter(name = 'UvCLdagger4x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv1x4)',
                          texname = '\\text{UvCLdagger4x1}')

UvCLdagger4x2 = Parameter(name = 'UvCLdagger4x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv2x4)',
                          texname = '\\text{UvCLdagger4x2}')

UvCLdagger4x3 = Parameter(name = 'UvCLdagger4x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv3x4)',
                          texname = '\\text{UvCLdagger4x3}')

UvCLdagger5x1 = Parameter(name = 'UvCLdagger5x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv1x5)',
                          texname = '\\text{UvCLdagger5x1}')

UvCLdagger5x2 = Parameter(name = 'UvCLdagger5x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv2x5)',
                          texname = '\\text{UvCLdagger5x2}')

UvCLdagger5x3 = Parameter(name = 'UvCLdagger5x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv3x5)',
                          texname = '\\text{UvCLdagger5x3}')

UvCL1x1 = Parameter(name = 'UvCL1x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv1x1',
                    texname = '\\text{UvCL1x1}')

UvCL1x2 = Parameter(name = 'UvCL1x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv1x2',
                    texname = '\\text{UvCL1x2}')

UvCL1x3 = Parameter(name = 'UvCL1x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv1x3',
                    texname = '\\text{UvCL1x3}')

UvCL2x1 = Parameter(name = 'UvCL2x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv2x1',
                    texname = '\\text{UvCL2x1}')

UvCL2x2 = Parameter(name = 'UvCL2x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv2x2',
                    texname = '\\text{UvCL2x2}')

UvCL2x3 = Parameter(name = 'UvCL2x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv2x3',
                    texname = '\\text{UvCL2x3}')

UvCL3x1 = Parameter(name = 'UvCL3x1',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv3x1',
                    texname = '\\text{UvCL3x1}')

UvCL3x2 = Parameter(name = 'UvCL3x2',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv3x2',
                    texname = '\\text{UvCL3x2}')

UvCL3x3 = Parameter(name = 'UvCL3x3',
                    nature = 'internal',
                    type = 'complex',
                    value = 'Uv3x3',
                    texname = '\\text{UvCL3x3}')

UvCLdagger1x1 = Parameter(name = 'UvCLdagger1x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv1x1)',
                          texname = '\\text{UvCLdagger1x1}')

UvCLdagger1x2 = Parameter(name = 'UvCLdagger1x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv2x1)',
                          texname = '\\text{UvCLdagger1x2}')

UvCLdagger1x3 = Parameter(name = 'UvCLdagger1x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv3x1)',
                          texname = '\\text{UvCLdagger1x3}')

UvCLdagger2x1 = Parameter(name = 'UvCLdagger2x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv1x2)',
                          texname = '\\text{UvCLdagger2x1}')

UvCLdagger2x2 = Parameter(name = 'UvCLdagger2x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv2x2)',
                          texname = '\\text{UvCLdagger2x2}')

UvCLdagger2x3 = Parameter(name = 'UvCLdagger2x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv3x2)',
                          texname = '\\text{UvCLdagger2x3}')

UvCLdagger3x1 = Parameter(name = 'UvCLdagger3x1',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv1x3)',
                          texname = '\\text{UvCLdagger3x1}')

UvCLdagger3x2 = Parameter(name = 'UvCLdagger3x2',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv2x3)',
                          texname = '\\text{UvCLdagger3x2}')

UvCLdagger3x3 = Parameter(name = 'UvCLdagger3x3',
                          nature = 'internal',
                          type = 'complex',
                          value = 'complexconjugate(Uv3x3)',
                          texname = '\\text{UvCLdagger3x3}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

v = Parameter(name = 'v',
              nature = 'internal',
              type = 'real',
              value = '(2*MW*sw)/ee',
              texname = 'v')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*v**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/v',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/v',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/v',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/v',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/v',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/v',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/v',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/v',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/v',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*v**2)',
                texname = '\\mu')

