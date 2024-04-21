from setuptools import find_packages, setup

package_name = 'automatic_dog_feeder'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['PIRsensor = automatic_dog_feeder.PIRsensor:main',
        'video_recording_node = automatic_dog_feeder.video_recording_node:main'
        ],
    },
)
