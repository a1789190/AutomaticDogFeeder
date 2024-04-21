# Use the official ROS 2 Docker image as the base
FROM ros:iron

# Set the working directory in the container
WORKDIR /ros2_ws

# Copy the ROS 2 package(s) into the container
COPY ros2_packages /ros2_ws/src/ros2_packages

# Install dependencies for building the ROS 2 package(s)
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# Build the ROS 2 package(s)
RUN . /opt/ros/foxy/setup.sh && \
    cd /ros2_ws && \
    colcon build

# Source ROS 2 setup.bash when the container launches
CMD ["bash", "-c", "source /opt/ros/iron/setup.bash && source /ros2_ws/install/setup.bash && ros2 run automatic_dog_feeder PIRsensor && ros2 run automatic_dog_feeder video_recording_node"]
