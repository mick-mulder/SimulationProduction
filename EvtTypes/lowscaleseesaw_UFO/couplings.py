# This file was automatically created by FeynRules 2.0.33
# Mathematica version: 9.0 for Linux x86 (64-bit) (February 7, 2013)
# Date: Fri 24 Jul 2015 10:44:58


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '-G',
                order = {'QCD':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_7 = Coupling(name = 'GC_7',
                value = 'cw*complex(0,1)*gw',
                order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '-(complex(0,1)*gw**2)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'cw**2*complex(0,1)*gw**2',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(cw*ee*complex(0,1))/(2.*sw)',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = 'complex(0,1)*gw*sw',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-2*cw*complex(0,1)*gw**2*sw',
                 order = {'QED':2})

GC_27 = Coupling(name = 'GC_27',
                 value = 'complex(0,1)*gw**2*sw**2',
                 order = {'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                 order = {'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(cw*ee*complex(0,1)*Theta1x1)/(2.*sw) + (ee*complex(0,1)*sw*Theta1x1)/(2.*cw)',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(cw*ee*complex(0,1)*Theta1x2)/(2.*sw) + (ee*complex(0,1)*sw*Theta1x2)/(2.*cw)',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(cw*ee*complex(0,1)*Theta1x3)/(2.*sw) + (ee*complex(0,1)*sw*Theta1x3)/(2.*cw)',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(cw*ee*complex(0,1)*Theta1x4)/(2.*sw) + (ee*complex(0,1)*sw*Theta1x4)/(2.*cw)',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(cw*ee*complex(0,1)*Theta1x5)/(2.*sw) + (ee*complex(0,1)*sw*Theta1x5)/(2.*cw)',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-(cw*ee*complex(0,1)*Theta2x1)/(2.*sw) - (ee*complex(0,1)*sw*Theta2x1)/(2.*cw)',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cw*ee*complex(0,1)*Theta2x2)/(2.*sw) + (ee*complex(0,1)*sw*Theta2x2)/(2.*cw)',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(cw*ee*complex(0,1)*Theta2x3)/(2.*sw) + (ee*complex(0,1)*sw*Theta2x3)/(2.*cw)',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cw*ee*complex(0,1)*Theta2x4)/(2.*sw) + (ee*complex(0,1)*sw*Theta2x4)/(2.*cw)',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(cw*ee*complex(0,1)*Theta2x5)/(2.*sw) + (ee*complex(0,1)*sw*Theta2x5)/(2.*cw)',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-(cw*ee*complex(0,1)*Theta3x1)/(2.*sw) - (ee*complex(0,1)*sw*Theta3x1)/(2.*cw)',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-(cw*ee*complex(0,1)*Theta3x2)/(2.*sw) - (ee*complex(0,1)*sw*Theta3x2)/(2.*cw)',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(cw*ee*complex(0,1)*Theta3x3)/(2.*sw) + (ee*complex(0,1)*sw*Theta3x3)/(2.*cw)',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(cw*ee*complex(0,1)*Theta3x4)/(2.*sw) + (ee*complex(0,1)*sw*Theta3x4)/(2.*cw)',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(cw*ee*complex(0,1)*Theta3x5)/(2.*sw) + (ee*complex(0,1)*sw*Theta3x5)/(2.*cw)',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(cw*ee*complex(0,1)*Theta4x1)/(2.*sw) - (ee*complex(0,1)*sw*Theta4x1)/(2.*cw)',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(cw*ee*complex(0,1)*Theta4x2)/(2.*sw) - (ee*complex(0,1)*sw*Theta4x2)/(2.*cw)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-(cw*ee*complex(0,1)*Theta4x3)/(2.*sw) - (ee*complex(0,1)*sw*Theta4x3)/(2.*cw)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(cw*ee*complex(0,1)*Theta4x4)/(2.*sw) + (ee*complex(0,1)*sw*Theta4x4)/(2.*cw)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(cw*ee*complex(0,1)*Theta4x5)/(2.*sw) + (ee*complex(0,1)*sw*Theta4x5)/(2.*cw)',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(cw*ee*complex(0,1)*Theta5x1)/(2.*sw) - (ee*complex(0,1)*sw*Theta5x1)/(2.*cw)',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-(cw*ee*complex(0,1)*Theta5x2)/(2.*sw) - (ee*complex(0,1)*sw*Theta5x2)/(2.*cw)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-(cw*ee*complex(0,1)*Theta5x3)/(2.*sw) - (ee*complex(0,1)*sw*Theta5x3)/(2.*cw)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(cw*ee*complex(0,1)*Theta5x4)/(2.*sw) - (ee*complex(0,1)*sw*Theta5x4)/(2.*cw)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(cw*ee*complex(0,1)*Theta5x5)/(2.*sw) + (ee*complex(0,1)*sw*Theta5x5)/(2.*cw)',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '(ee*complex(0,1)*UvCL1x1)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee*complex(0,1)*UvCL1x2)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(ee*complex(0,1)*UvCL1x3)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(ee*complex(0,1)*UvCL1x4)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(ee*complex(0,1)*UvCL1x5)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(ee*complex(0,1)*UvCL2x1)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(ee*complex(0,1)*UvCL2x2)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(ee*complex(0,1)*UvCL2x3)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(ee*complex(0,1)*UvCL2x4)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '(ee*complex(0,1)*UvCL2x5)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee*complex(0,1)*UvCL3x1)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(ee*complex(0,1)*UvCL3x2)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(ee*complex(0,1)*UvCL3x3)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(ee*complex(0,1)*UvCL3x4)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(ee*complex(0,1)*UvCL3x5)/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-((complex(0,1)*MN*Theta4x5)/v) - (complex(0,1)*MN*Theta5x4)/v',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-((complex(0,1)*MN*Theta1x4)/v)',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((complex(0,1)*MN*Theta1x5)/v)',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-((complex(0,1)*MN*Theta2x4)/v)',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-((complex(0,1)*MN*Theta2x5)/v)',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-((complex(0,1)*MN*Theta3x4)/v)',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-((complex(0,1)*MN*Theta3x5)/v)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-((complex(0,1)*MN*Theta4x4)/v)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((complex(0,1)*MN*Theta5x5)/v)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-6*complex(0,1)*lam*v',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(ee**2*complex(0,1)*v)/(2.*sw**2)',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = 'ee**2*complex(0,1)*v + (cw**2*ee**2*complex(0,1)*v)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*v)/(2.*cw**2)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((complex(0,1)*MN*complexconjugate(Theta1x4))/v)',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '-((complex(0,1)*MN*complexconjugate(Theta1x5))/v)',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((complex(0,1)*MN*complexconjugate(Theta2x4))/v)',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-((complex(0,1)*MN*complexconjugate(Theta2x5))/v)',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((complex(0,1)*MN*complexconjugate(Theta3x4))/v)',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-((complex(0,1)*MN*complexconjugate(Theta3x5))/v)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((complex(0,1)*MN*complexconjugate(Theta4x4))/v)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-((complex(0,1)*MN*complexconjugate(Theta4x5))/v) - (complex(0,1)*MN*complexconjugate(Theta5x4))/v',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-((complex(0,1)*MN*complexconjugate(Theta5x5))/v)',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL1x4))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL1x5))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL2x4))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL2x5))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL3x4))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '(ee*complex(0,1)*complexconjugate(UvCL3x5))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

