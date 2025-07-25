from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument


def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "lidar_topic",
                default_value="/cloud",
                description="",
            ),
            DeclareLaunchArgument(
                "use_2d_lidar",
                default_value="false",
                description="",
                choices=["true", "false"],
            ),
            DeclareLaunchArgument(
                "lidar_odometry_topic",
                default_value="lidar_odometry",
                description="",
            ),
            DeclareLaunchArgument(
                "lidar_odom_frame",
                default_value="ranger/base_link",
                description="",
            ),
            DeclareLaunchArgument(
                "wheel_odom_frame",
                default_value="ranger/odom",
                description="",
            ),
            DeclareLaunchArgument(
                "base_frame",
                default_value="ranger/base_footprint",
                description="",
            ),
            DeclareLaunchArgument(
                "publish_odom_tf",
                default_value="false",
                description="",
                choices=["true", "false"],
            ),
            DeclareLaunchArgument(
                "invert_odom_tf",
                default_value="true",
                description="",
                choices=["true", "false"],
            ),
            DeclareLaunchArgument(
                "visualize",
                default_value="true",
                description="",
                choices=["true", "false"],
            ),
        ]
    )
