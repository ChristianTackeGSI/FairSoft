# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
#   Spack Project Developers. See the top-level COPYRIGHT file for details.
# Copyright 2020-2021 GSI Helmholtz Centre for Heavy Ion Research GmbH,
#   Darmstadt, Germany
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)



class FairsoftBundle(BundlePackage):
    homepage = "https://github.com/FairRootGroup/FairSoft"

    version('21.3')
    version('20.11')
    version('19.6')

    variant('graphics', default=False)

    depends_on('root +fortran+gdml+pythia6+pythia8+vc~vdt+python+tmva+mlp+xrootd+sqlite')
    depends_on('root +spectrum', when='@20.11:')
    depends_on('root +x+opengl', when='+graphics')
    depends_on('root +aqua', when='+graphics platform=darwin')

    # mar21:
    depends_on('root@6.22.06', when='@21.3')
    depends_on('fairsoft-config@nov20', type='run', when='@21.3')

    # nov20:
    depends_on('root@6.20.08', when='@20.11')
    depends_on('fairsoft-config@nov20', type='run', when='@20.11')

    # jun19:
    depends_on('root@6.16.00 +memstat', when='@19.6')
    depends_on('fairsoft-config@jun19', type='run', when='@19.6')
