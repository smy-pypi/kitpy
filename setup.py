import kitpylib as kpl

kpl.smy_setup(kpl,
              author=kpl.smyinfo['author'],
              author_email=kpl.smyinfo['author_email'],
              license=kpl.__copr__,
            install_requires=["numpy>=1.26.4",
                              "matplotlib>=3.9.2",
                              "scipy>=1.13.1",
                              "setuptools>=72.1.0"
                              ],
            package_data={'kitpylib': ['PyPlot/*.png']},
            include_package_data=True,
            description='A Python Toolkit Library for developing packages',
            python_requires='>=3.9',
            download_url='https://pypi.org/project/kitpylib/#files',
            url='https://pypi.org/project/kitpylib/'
            )