# vacuum-workspace-source.tar.gz

Historical source: ros-resumed


## src

## src/vacuum_sim

## src/vacuum_sim/package.xml

<?xml version="1.0"?>
<package format="3">
  <name>vacuum_sim</name><version>0.1.0</version>
  <description>Starter vacuum robot simulation with explicitly provisional geometry.</description>
  <maintainer email="[REDACTED_EMAIL]">Local robot developer</maintainer>
  <license>Apache-2.0</license>
  <buildtool_depend>ament_cmake</buildtool_depend>
  <exec_depend>ament_index_python</exec_depend><exec_depend>launch</exec_depend><exec_depend>launch_ros</exec_depend>
  <exec_depend>rclpy</exec_depend><exec_depend>geometry_msgs</exec_depend>
  <exec_depend>robot_state_publisher</exec_depend><exec_depend>xacro</exec_depend>
  <exec_depend>ros_gz_sim</exec_depend><exec_depend>ros_gz_bridge</exec_depend>
  <exec_depend>gz_ros2_control</exec_depend><exec_depend>controller_manager</exec_depend>
  <exec_depend>diff_drive_controller</exec_depend><exec_depend>joint_state_broadcaster</exec_depend>
  <exec_depend>rviz2</exec_depend><exec_depend>slam_toolbox</exec_depend>
  <exec_depend>nav2_bringup</exec_depend><exec_depend>python3-yaml</exec_depend>
  <export><build_type>ament_cmake</build_type></export>
</package>


## src/vacuum_sim/config

## src/vacuum_sim/config/view.rviz

Panels:
- Class: rviz_common/Displays
  Help Height: 70
  Name: Displays
  Property Tree Widget:
    Expanded: null
    Splitter Ratio: 0.5
  Tree Height: 208
- Class: rviz_common/Tool Properties
  Expanded: null
  Name: Tool Properties
  Splitter Ratio: 0.5
Visualization Manager:
  Class: ''
  Displays:
  - Alpha: 0.5
    Cell Size: 0.5
    Class: rviz_default_plugins/Grid
    Color: 160; 160; 164
    Enabled: true
    Line Style:
      Line Width: 0.029999999329447746
      Value: Lines
    Name: Grid
    Normal Cell Count: 0
    Offset:
      X: 0
      Y: 0
      Z: 0
    Plane: XY
    Plane Cell Count: 20
    Reference Frame: <Fixed Frame>
    Value: true
  - Alpha: 1
    Class: rviz_default_plugins/RobotModel
    Collision Enabled: false
    Description File: ''
    Description Source: Topic
    Description Topic:
      Depth: 5
      Durability Policy: Transient Local
      History Policy: Keep Last
      Reliability Policy: Reliable
      Value: /robot_description
    Enabled: true
    Links:
      All Links Enabled: true
      Expand Joint Details: false
      Expand Link Details: false
      Expand Tree: false
      Link Tree Style: Links in Alphabetic Order
      base_footprint:
        Alpha: 1
        Show Axes: false
        Show Trail: false
      base_link:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
      camera_link:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
      camera_optical_frame:
        Alpha: 1
        Show Axes: false
        Show Trail: false
      caster:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
      left_wheel:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
      lidar_link:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
      right_wheel:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
    Mass Properties:
      Inertia: false
      Mass: false
    Name: Robot
    TF Prefix: ''
    Update Interval: 0
    Value: true
    Visual Enabled: true
  - Alpha: 1
    Autocompute Intensity Bounds: true
    Autocompute Value Bounds:
      Max Value: 10
      Min Value: -10
      Value: true
    Axis: Z
    Channel Name: intensity
    Class: rviz_default_plugins/LaserScan
    Color: 255; 255; 255
    Color Transformer: Intensity
    Decay Time: 0
    Enabled: true
    Invert Rainbow: false
    Max Color: 255; 255; 255
    Max Intensity: 0
    Min Color: 0; 0; 0
    Min Intensity: 0
    Name: Lidar
    Position Transformer: XYZ
    Selectable: true
    Size (Pixels): 3
    Size (m): 0.02500000037252903
    Style: Flat Squares
    Topic:
      Depth: 5
      Durability Policy: Volatile
      Filter size: 10
      History Policy: Keep Last
      Reliability Policy: Best Effort
      Value: /scan
    Use Fixed Frame: true
    Use rainbow: true
    Value: true
  - Alpha: 0.699999988079071
    Binary representation: false
    Binary threshold: 100
    Class: rviz_default_plugins/Map
    Color Scheme: map
    Draw Behind: false
    Enabled: true
    Name: Map
    Topic:
      Depth: 5
      Durability Policy: Transient Local
      Filter size: 10
      History Policy: Keep Last
      Reliability Policy: Reliable
      Value: /map
    Update Topic:
      Depth: 5
      Durability Policy: Volatile
      History Policy: Keep Last
      Reliability Policy: Reliable
      Value: /map_updates
    Use Timestamp: false
    Value: true
  - Class: rviz_default_plugins/Image
    Enabled: true
    Max Value: 1
    Median window: 5
    Min Value: 0
    Name: Camera
    Normalize Range: true
    Topic:
      Depth: 5
      Durability Policy: Volatile
      History Policy: Keep Last
      Reliability Policy: Best Effort
      Value: /camera/image_raw
    Value: true
  Enabled: true
  Global Options:
    Background Color: 35; 40; 48
    Fixed Frame: map
    Frame Rate: 60
  Name: root
  Tools:
  - Class: rviz_default_plugins/Interact
    Hide Inactive Objects: true
  - Class: rviz_default_plugins/MoveCamera
  - Class: rviz_default_plugins/Select
  - Class: nav2_rviz_plugins/GoalTool
  Transformation:
    Current:
      Class: rviz_default_plugins/TF
  Value: true
  Views:
    Current:
      Class: rviz_default_plugins/Orbit
      Distance: 6
      Enable Stereo Rendering:
        Stereo Eye Separation: 0.05999999865889549
        Stereo Focal Distance: 1
        Swap Stereo Eyes: false
        Value: false
      Focal Point:
        X: 0
        Y: 0
        Z: 0
      Focal Shape Fixed Size: true
      Focal Shape Size: 0.05000000074505806
      Invert Z Axis: false
      Name: Current View
      Near Clip Distance: 0.009999999776482582
      Pitch: 0.800000011920929
      Target Frame: <Fixed Frame>
      Value: Orbit (rviz_default_plugins)
      Yaw: 0.800000011920929
    Saved: null
Window Geometry:
  Camera:
    collapsed: false
  Displays:
    collapsed: false
  Height: 800
  Hide Left Dock: false
  Hide Right Dock: false
  QMainWindow State: 000000ff00000000fd000000010000000000000156000002cafc0200000003fb0000000c00430061006d006500720061010000003b000000c90000001600fffffffb000000100044006900730070006c006100790073010000010a00000151000000c700fffffffb0000001e0054006f006f006c002000500072006f00700065007200740069006500730100000261000000a40000005c00ffffff00000354000002ca00000004000000040000000800000008fc0000000100000002000000010000000a0054006f006f006c00730100000000ffffffff0000000000000000
  Tool Properties:
    collapsed: false
  Width: 1200
  X: 1934
  Y: 40


## src/vacuum_sim/config/bridge.yaml

- ros_topic_name: /clock
  gz_topic_name: /clock
  ros_type_name: rosgraph_msgs/msg/Clock
  gz_type_name: gz.msgs.Clock
  direction: GZ_TO_ROS
- ros_topic_name: /scan
  gz_topic_name: /scan
  ros_type_name: sensor_msgs/msg/LaserScan
  gz_type_name: gz.msgs.LaserScan
  direction: GZ_TO_ROS
  qos_profile: SENSOR_DATA
- ros_topic_name: /camera/image_raw
  gz_topic_name: /camera/image_raw
  ros_type_name: sensor_msgs/msg/Image
  gz_type_name: gz.msgs.Image
  direction: GZ_TO_ROS
  qos_profile: SENSOR_DATA
- ros_topic_name: /camera/camera_info
  gz_topic_name: /camera/camera_info
  ros_type_name: sensor_msgs/msg/CameraInfo
  gz_type_name: gz.msgs.CameraInfo
  direction: GZ_TO_ROS
  qos_profile: SENSOR_DATA


## src/vacuum_sim/config/nav2.yaml

amcl:
  ros__parameters:
    alpha1: 0.2
    alpha2: 0.2
    alpha3: 0.2
    alpha4: 0.2
    alpha5: 0.2
    base_frame_id: base_footprint
    beam_skip_distance: 0.5
    beam_skip_error_threshold: 0.9
    beam_skip_threshold: 0.3
    do_beamskip: false
    global_frame_id: map
    lambda_short: 0.1
    laser_likelihood_max_dist: 2.0
    laser_max_range: 100.0
    laser_min_range: -1.0
    laser_model_type: likelihood_field
    max_beams: 60
    max_particles: 2000
    min_particles: 500
    odom_frame_id: odom
    pf_err: 0.05
    pf_z: 0.99
    recovery_alpha_fast: 0.0
    recovery_alpha_slow: 0.0
    resample_interval: 1
    robot_model_type: nav2_amcl::DifferentialMotionModel
    save_pose_rate: 0.5
    sigma_hit: 0.2
    tf_broadcast: true
    transform_tolerance: 1.0
    update_min_a: 0.2
    update_min_d: 0.25
    z_hit: 0.5
    z_max: 0.05
    z_rand: 0.5
    z_short: 0.05
    scan_topic: scan
    use_sim_time: true
bt_navigator:
  ros__parameters:
    global_frame: map
    robot_base_frame: base_footprint
    odom_topic: /odom
    bt_loop_duration: 10
    default_server_timeout: 20
    wait_for_service_timeout: 1000
    action_server_result_timeout: 900.0
    navigators:
    - navigate_to_pose
    - navigate_through_poses
    navigate_to_pose:
      plugin: nav2_bt_navigator::NavigateToPoseNavigator
    navigate_through_poses:
      plugin: nav2_bt_navigator::NavigateThroughPosesNavigator
    error_code_names:
    - compute_path_error_code
    - follow_path_error_code
    use_sim_time: true
    enable_stamped_cmd_vel: false
controller_server:
  ros__parameters:
    controller_frequency: 20.0
    costmap_update_timeout: 0.3
    min_x_velocity_threshold: 0.001
    min_y_velocity_threshold: 0.5
    min_theta_velocity_threshold: 0.001
    failure_tolerance: 0.3
    progress_checker_plugins:
    - progress_checker
    goal_checker_plugins:
    - general_goal_checker
    controller_plugins:
    - FollowPath
    use_realtime_priority: false
    progress_checker:
      plugin: nav2_controller::SimpleProgressChecker
      required_movement_radius: 0.15
      movement_time_allowance: 30.0
    general_goal_checker:
      stateful: true
      plugin: nav2_controller::SimpleGoalChecker
      xy_goal_tolerance: 0.15
      yaw_goal_tolerance: 0.25
    FollowPath:
      plugin: dwb_core::DWBLocalPlanner
      debug_trajectory_details: false
      min_vel_x: -0.15
      max_vel_x: 0.25
      min_vel_y: 0.0
      max_vel_y: 0.0
      max_vel_theta: 1.0
      min_speed_xy: 0.0
      max_speed_xy: 0.25
      min_speed_theta: 0.0
      acc_lim_x: 0.3
      acc_lim_y: 0.0
      acc_lim_theta: 1.0
      decel_lim_x: -0.3
      decel_lim_y: 0.0
      decel_lim_theta: -1.0
      vx_samples: 20
      vy_samples: 1
      vtheta_samples: 20
      sim_time: 1.7
      linear_granularity: 0.05
      angular_granularity: 0.025
      transform_tolerance: 0.2
      xy_goal_tolerance: 0.15
      trans_stopped_velocity: 0.02
      short_circuit_trajectory_evaluation: true
      stateful: true
      critics:
      - RotateToGoal
      - Oscillation
      - BaseObstacle
      - GoalAlign
      - PathAlign
      - PathDist
      - GoalDist
      BaseObstacle.scale: 0.02
      PathAlign.scale: 32.0
      PathAlign.forward_point_distance: 0.1
      GoalAlign.scale: 24.0
      GoalAlign.forward_point_distance: 0.1
      PathDist.scale: 32.0
      GoalDist.scale: 24.0
      RotateToGoal.scale: 32.0
      RotateToGoal.slowing_factor: 5.0
      RotateToGoal.lookahead_time: -1.0
    use_sim_time: true
    odom_topic: /odom
    enable_stamped_cmd_vel: false
local_costmap:
  local_costmap:
    ros__parameters:
      update_frequency: 5.0
      publish_frequency: 2.0
      global_frame: odom
      robot_base_frame: base_footprint
      rolling_window: true
      width: 3
      height: 3
      resolution: 0.05
      plugins:
      - voxel_layer
      - inflation_layer
      inflation_layer:
        plugin: nav2_costmap_2d::InflationLayer
        cost_scaling_factor: 3.0
        inflation_radius: 0.35
      voxel_layer:
        plugin: nav2_costmap_2d::VoxelLayer
        enabled: true
        publish_voxel_map: true
        origin_z: 0.0
        z_resolution: 0.05
        z_voxels: 16
        max_obstacle_height: 2.0
        mark_threshold: 0
        observation_sources: scan
        scan:
          topic: /scan
          max_obstacle_height: 2.0
          clearing: true
          marking: true
          data_type: LaserScan
          raytrace_max_range: 8.0
          raytrace_min_range: 0.0
          obstacle_max_range: 6.0
          obstacle_min_range: 0.0
      static_layer:
        plugin: nav2_costmap_2d::StaticLayer
        map_subscribe_transient_local: true
      always_send_full_costmap: true
      use_sim_time: true
      footprint: '[[0.120726, 0.0], [0.11783, 0.029405], [0.109252, 0.05768], [0.095324,
        0.083739], [0.076579, 0.106579], [0.053739, 0.125324], [0.02768, 0.139252],
        [-0.000595, 0.14783], [-0.03, 0.150726], [-0.059405, 0.14783], [-0.08768,
        0.139252], [-0.113739, 0.125324], [-0.136579, 0.106579], [-0.155324, 0.083739],
        [-0.169252, 0.05768], [-0.17783, 0.029405], [-0.180726, 0.0], [-0.17783, -0.029405],
        [-0.169252, -0.05768], [-0.155324, -0.083739], [-0.136579, -0.106579], [-0.113739,
        -0.125324], [-0.08768, -0.139252], [-0.059405, -0.14783], [-0.03, -0.150726],
        [-0.000595, -0.14783], [0.02768, -0.139252], [0.053739, -0.125324], [0.076579,
        -0.106579], [0.095324, -0.083739], [0.109252, -0.05768], [0.11783, -0.029405]]'
      footprint_padding: 0.02
global_costmap:
  global_costmap:
    ros__parameters:
      update_frequency: 1.0
      publish_frequency: 1.0
      global_frame: map
      robot_base_frame: base_footprint
      resolution: 0.05
      track_unknown_space: true
      plugins:
      - static_layer
      - obstacle_layer
      - inflation_layer
      obstacle_layer:
        plugin: nav2_costmap_2d::ObstacleLayer
        enabled: true
        observation_sources: scan
        scan:
          topic: /scan
          max_obstacle_height: 2.0
          clearing: true
          marking: true
          data_type: LaserScan
          raytrace_max_range: 8.0
          raytrace_min_range: 0.0
          obstacle_max_range: 6.0
          obstacle_min_range: 0.0
      static_layer:
        plugin: nav2_costmap_2d::StaticLayer
        map_subscribe_transient_local: true
      inflation_layer:
        plugin: nav2_costmap_2d::InflationLayer
        cost_scaling_factor: 3.0
        inflation_radius: 0.35
      always_send_full_costmap: true
      use_sim_time: true
      footprint: '[[0.120726, 0.0], [0.11783, 0.029405], [0.109252, 0.05768], [0.095324,
        0.083739], [0.076579, 0.106579], [0.053739, 0.125324], [0.02768, 0.139252],
        [-0.000595, 0.14783], [-0.03, 0.150726], [-0.059405, 0.14783], [-0.08768,
        0.139252], [-0.113739, 0.125324], [-0.136579, 0.106579], [-0.155324, 0.083739],
        [-0.169252, 0.05768], [-0.17783, 0.029405], [-0.180726, 0.0], [-0.17783, -0.029405],
        [-0.169252, -0.05768], [-0.155324, -0.083739], [-0.136579, -0.106579], [-0.113739,
        -0.125324], [-0.08768, -0.139252], [-0.059405, -0.14783], [-0.03, -0.150726],
        [-0.000595, -0.14783], [0.02768, -0.139252], [0.053739, -0.125324], [0.076579,
        -0.106579], [0.095324, -0.083739], [0.109252, -0.05768], [0.11783, -0.029405]]'
      footprint_padding: 0.02
map_saver:
  ros__parameters:
    save_map_timeout: 5.0
    free_thresh_default: 0.25
    occupied_thresh_default: 0.65
    map_subscribe_transient_local: true
    use_sim_time: true
planner_server:
  ros__parameters:
    expected_planner_frequency: 20.0
    planner_plugins:
    - GridBased
    costmap_update_timeout: 1.0
    GridBased:
      plugin: nav2_navfn_planner::NavfnPlanner
      tolerance: 0.5
      use_astar: false
      allow_unknown: false
    use_sim_time: true
smoother_server:
  ros__parameters:
    smoother_plugins:
    - simple_smoother
    simple_smoother:
      plugin: nav2_smoother::SimpleSmoother
      tolerance: 1.0e-10
      max_its: 1000
      do_refinement: true
    use_sim_time: true
behavior_server:
  ros__parameters:
    local_costmap_topic: local_costmap/costmap_raw
    global_costmap_topic: global_costmap/costmap_raw
    local_footprint_topic: local_costmap/published_footprint
    global_footprint_topic: global_costmap/published_footprint
    cycle_frequency: 10.0
    behavior_plugins:
    - spin
    - backup
    - drive_on_heading
    - assisted_teleop
    - wait
    spin:
      plugin: nav2_behaviors::Spin
    backup:
      plugin: nav2_behaviors::BackUp
    drive_on_heading:
      plugin: nav2_behaviors::DriveOnHeading
    wait:
      plugin: nav2_behaviors::Wait
    assisted_teleop:
      plugin: nav2_behaviors::AssistedTeleop
    local_frame: odom
    global_frame: map
    robot_base_frame: base_footprint
    transform_tolerance: 0.1
    simulate_ahead_time: 2.0
    max_rotational_vel: 1.0
    min_rotational_vel: 0.4
    rotational_acc_lim: 3.2
    use_sim_time: true
    odom_topic: /odom
    enable_stamped_cmd_vel: false
waypoint_follower:
  ros__parameters:
    loop_rate: 20
    stop_on_failure: false
    action_server_result_timeout: 900.0
    waypoint_task_executor_plugin: wait_at_waypoint
    wait_at_waypoint:
      plugin: nav2_waypoint_follower::WaitAtWaypoint
      enabled: true
      waypoint_pause_duration: 200
    use_sim_time: true
route_server:
  ros__parameters:
    boundary_radius_to_achieve_node: 1.0
    radius_to_achieve_node: 2.0
    smooth_corners: true
    operations:
    - AdjustSpeedLimit
    - ReroutingService
    - CollisionMonitor
    ReroutingService:
      plugin: nav2_route::ReroutingService
    AdjustSpeedLimit:
      plugin: nav2_route::AdjustSpeedLimit
    CollisionMonitor:
      plugin: nav2_route::CollisionMonitor
      max_collision_dist: 3.0
    edge_cost_functions:
    - DistanceScorer
    - CostmapScorer
    DistanceScorer:
      plugin: nav2_route::DistanceScorer
    CostmapScorer:
      plugin: nav2_route::CostmapScorer
    use_sim_time: true
velocity_smoother:
  ros__parameters:
    smoothing_frequency: 20.0
    stamp_smoothed_velocity_with_smoothing_time: false
    scale_velocities: false
    feedback: OPEN_LOOP
    max_velocity:
    - 0.25
    - 0.0
    - 1.0
    min_velocity:
    - -0.15
    - 0.0
    - -1.0
    max_accel:
    - 0.3
    - 0.0
    - 1.0
    max_decel:
    - -0.3
    - 0.0
    - -1.0
    odom_topic: /odom
    odom_duration: 0.1
    deadband_velocity:
    - 0.0
    - 0.0
    - 0.0
    velocity_timeout: 0.5
    use_sim_time: true
    enable_stamped_cmd_vel: false
collision_monitor:
  ros__parameters:
    base_frame_id: base_footprint
    odom_frame_id: odom
    cmd_vel_in_topic: cmd_vel_smoothed
    cmd_vel_out_topic: cmd_vel
    state_topic: collision_monitor_state
    transform_tolerance: 0.2
    source_timeout: 1.0
    base_shift_correction: true
    stop_pub_timeout: 2.0
    polygons:
    - FootprintApproach
    FootprintApproach:
      type: polygon
      action_type: approach
      footprint_topic: /local_costmap/published_footprint
      time_before_collision: 0.55
      simulation_time_step: 0.02
      min_points: 6
      visualize: false
      enabled: true
    observation_sources:
    - scan
    scan:
      type: scan
      topic: scan
      min_height: 0.15
      max_height: 2.0
      enabled: true
    use_sim_time: true
    enable_stamped_cmd_vel: false
docking_server:
  ros__parameters:
    controller_frequency: 50.0
    initial_perception_timeout: 5.0
    wait_charge_timeout: 5.0
    dock_approach_timeout: 30.0
    undock_linear_tolerance: 0.05
    undock_angular_tolerance: 0.1
    max_retries: 3
    base_frame: base_footprint
    fixed_frame: odom
    dock_backwards: false
    dock_prestaging_tolerance: 0.5
    dock_plugins:
    - simple_charging_dock
    simple_charging_dock:
      plugin: opennav_docking::SimpleChargingDock
      docking_threshold: 0.05
      staging_x_offset: -0.7
      use_external_detection_pose: true
      use_battery_status: false
      use_stall_detection: false
      external_detection_timeout: 1.0
      external_detection_translation_x: -0.18
      external_detection_translation_y: 0.0
      external_detection_rotation_roll: -1.57
      external_detection_rotation_pitch: -1.57
      external_detection_rotation_yaw: 0.0
      filter_coef: 0.1
    controller:
      k_phi: 3.0
      k_delta: 2.0
      v_linear_min: 0.15
      v_linear_max: 0.15
      use_collision_detection: true
      costmap_topic: local_costmap/costmap_raw
      footprint_topic: local_costmap/published_footprint
      transform_tolerance: 0.1
      projection_time: 5.0
      simulation_step: 0.1
      dock_collision_threshold: 0.3
    use_sim_time: true
    enable_stamped_cmd_vel: false
loopback_simulator:
  ros__parameters:
    base_frame_id: base_footprint
    odom_frame_id: odom
    map_frame_id: map
    scan_frame_id: base_scan
    update_duration: 0.02
    scan_range_min: 0.05
    scan_range_max: 30.0
    scan_angle_min: -3.1415
    scan_angle_max: 3.1415
    scan_angle_increment: 0.02617
    scan_use_inf: true
    use_sim_time: true


## src/vacuum_sim/config/vacuum_navigate.xml

<root BTCPP_format="4" main_tree_to_execute="MainTree">
  <BehaviorTree ID="MainTree">
    <RecoveryNode number_of_retries="2" name="BoundedWaitAndReplan">
      <PipelineSequence name="NavigateWithReplanning">
        <RateController hz="1.0">
          <ComputePathToPose goal="{goal}" path="{path}" planner_id="GridBased" error_code_id="{compute_path_error_code}"/>
        </RateController>
        <FollowPath path="{path}" controller_id="FollowPath" error_code_id="{follow_path_error_code}"/>
      </PipelineSequence>
      <Wait wait_duration="3.0"/>
    </RecoveryNode>
  </BehaviorTree>
</root>


## src/vacuum_sim/config/slam.yaml

slam_toolbox:
  ros__parameters:
    use_sim_time: true
    mode: mapping
    odom_frame: odom
    map_frame: map
    base_frame: base_footprint
    scan_topic: /scan
    resolution: 0.05
    max_laser_range: 12.0
    minimum_travel_distance: 0.1
    minimum_travel_heading: 0.15
    map_update_interval: 2.0
    transform_publish_period: 0.02
    transform_timeout: 0.2
    tf_buffer_duration: 30.0
    scan_queue_size: 1
    use_scan_matching: true
    use_scan_barycenter: true
    solver_plugin: solver_plugins::CeresSolver
    ceres_linear_solver: SPARSE_NORMAL_CHOLESKY
    ceres_preconditioner: SCHUR_JACOBI
    ceres_trust_strategy: LEVENBERG_MARQUARDT
    ceres_dogleg_type: TRADITIONAL_DOGLEG
    ceres_loss_function: None


## src/vacuum_sim/config/drive.rviz

Panels:
- Class: rviz_common/Displays
  Help Height: 70
  Name: Displays
  Property Tree Widget:
    Expanded: null
    Splitter Ratio: 0.5
  Tree Height: 208
- Class: rviz_common/Tool Properties
  Expanded: null
  Name: Tool Properties
  Splitter Ratio: 0.5
Visualization Manager:
  Class: ''
  Displays:
  - Alpha: 0.5
    Cell Size: 0.5
    Class: rviz_default_plugins/Grid
    Color: 160; 160; 164
    Enabled: true
    Line Style:
      Line Width: 0.029999999329447746
      Value: Lines
    Name: Grid
    Normal Cell Count: 0
    Offset:
      X: 0
      Y: 0
      Z: 0
    Plane: XY
    Plane Cell Count: 20
    Reference Frame: <Fixed Frame>
    Value: true
  - Alpha: 1
    Class: rviz_default_plugins/RobotModel
    Collision Enabled: false
    Description File: ''
    Description Source: Topic
    Description Topic:
      Depth: 5
      Durability Policy: Transient Local
      History Policy: Keep Last
      Reliability Policy: Reliable
      Value: /robot_description
    Enabled: true
    Links:
      All Links Enabled: true
      Expand Joint Details: false
      Expand Link Details: false
      Expand Tree: false
      Link Tree Style: Links in Alphabetic Order
      base_footprint:
        Alpha: 1
        Show Axes: false
        Show Trail: false
      base_link:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
      camera_link:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
      camera_optical_frame:
        Alpha: 1
        Show Axes: false
        Show Trail: false
      caster:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
      left_wheel:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
      lidar_link:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
      right_wheel:
        Alpha: 1
        Show Axes: false
        Show Trail: false
        Value: true
    Mass Properties:
      Inertia: false
      Mass: false
    Name: Robot
    TF Prefix: ''
    Update Interval: 0
    Value: true
    Visual Enabled: true
  - Alpha: 1
    Autocompute Intensity Bounds: true
    Autocompute Value Bounds:
      Max Value: 10
      Min Value: -10
      Value: true
    Axis: Z
    Channel Name: intensity
    Class: rviz_default_plugins/LaserScan
    Color: 255; 255; 255
    Color Transformer: Intensity
    Decay Time: 0
    Enabled: true
    Invert Rainbow: false
    Max Color: 255; 255; 255
    Max Intensity: 0
    Min Color: 0; 0; 0
    Min Intensity: 0
    Name: Lidar
    Position Transformer: XYZ
    Selectable: true
    Size (Pixels): 3
    Size (m): 0.02500000037252903
    Style: Flat Squares
    Topic:
      Depth: 5
      Durability Policy: Volatile
      Filter size: 10
      History Policy: Keep Last
      Reliability Policy: Best Effort
      Value: /scan
    Use Fixed Frame: true
    Use rainbow: true
    Value: true
  - Class: rviz_default_plugins/Image
    Enabled: true
    Max Value: 1
    Median window: 5
    Min Value: 0
    Name: Camera
    Normalize Range: true
    Topic:
      Depth: 5
      Durability Policy: Volatile
      History Policy: Keep Last
      Reliability Policy: Best Effort
      Value: /camera/image_raw
    Value: true
  Enabled: true
  Global Options:
    Background Color: 35; 40; 48
    Fixed Frame: odom
    Frame Rate: 60
  Name: root
  Tools:
  - Class: rviz_default_plugins/Interact
    Hide Inactive Objects: true
  - Class: rviz_default_plugins/MoveCamera
  - Class: rviz_default_plugins/Select
  - Class: nav2_rviz_plugins/GoalTool
  Transformation:
    Current:
      Class: rviz_default_plugins/TF
  Value: true
  Views:
    Current:
      Class: rviz_default_plugins/Orbit
      Distance: 6
      Enable Stereo Rendering:
        Stereo Eye Separation: 0.05999999865889549
        Stereo Focal Distance: 1
        Swap Stereo Eyes: false
        Value: false
      Focal Point:
        X: 0
        Y: 0
        Z: 0
      Focal Shape Fixed Size: true
      Focal Shape Size: 0.05000000074505806
      Invert Z Axis: false
      Name: Current View
      Near Clip Distance: 0.009999999776482582
      Pitch: 0.800000011920929
      Target Frame: <Fixed Frame>
      Value: Orbit (rviz_default_plugins)
      Yaw: 0.800000011920929
    Saved: null
Window Geometry:
  Camera:
    collapsed: false
  Displays:
    collapsed: false
  Height: 800
  Hide Left Dock: false
  Hide Right Dock: false
  QMainWindow State: 000000ff00000000fd000000010000000000000156000002cafc0200000003fb0000000c00430061006d006500720061010000003b000000c90000001600fffffffb000000100044006900730070006c006100790073010000010a00000151000000c700fffffffb0000001e0054006f006f006c002000500072006f00700065007200740069006500730100000261000000a40000005c00ffffff00000354000002ca00000004000000040000000800000008fc0000000100000002000000010000000a0054006f006f006c00730100000000ffffffff0000000000000000
  Tool Properties:
    collapsed: false
  Width: 1200
  X: 1934
  Y: 40


## src/vacuum_sim/config/vacuum_nav2.yaml

amcl:
  ros__parameters:
    alpha1: 0.2
    alpha2: 0.2
    alpha3: 0.2
    alpha4: 0.2
    alpha5: 0.2
    base_frame_id: base_footprint
    beam_skip_distance: 0.5
    beam_skip_error_threshold: 0.9
    beam_skip_threshold: 0.3
    do_beamskip: false
    global_frame_id: map
    lambda_short: 0.1
    laser_likelihood_max_dist: 2.0
    laser_max_range: 100.0
    laser_min_range: -1.0
    laser_model_type: likelihood_field
    max_beams: 60
    max_particles: 2000
    min_particles: 500
    odom_frame_id: odom
    pf_err: 0.05
    pf_z: 0.99
    recovery_alpha_fast: 0.0
    recovery_alpha_slow: 0.0
    resample_interval: 1
    robot_model_type: nav2_amcl::DifferentialMotionModel
    save_pose_rate: 0.5
    sigma_hit: 0.2
    tf_broadcast: true
    transform_tolerance: 1.0
    update_min_a: 0.2
    update_min_d: 0.25
    z_hit: 0.5
    z_max: 0.05
    z_rand: 0.5
    z_short: 0.05
    scan_topic: scan
    use_sim_time: true
bt_navigator:
  ros__parameters:
    global_frame: map
    robot_base_frame: base_footprint
    odom_topic: /odom
    bt_loop_duration: 10
    default_server_timeout: 20
    wait_for_service_timeout: 1000
    action_server_result_timeout: 900.0
    navigators:
    - navigate_to_pose
    navigate_to_pose:
      plugin: nav2_bt_navigator::NavigateToPoseNavigator
    navigate_through_poses:
      plugin: nav2_bt_navigator::NavigateThroughPosesNavigator
    error_code_names:
    - compute_path_error_code
    - follow_path_error_code
    use_sim_time: true
    enable_stamped_cmd_vel: false
    default_nav_to_pose_bt_xml: /home/robot/vacuum_ws/src/vacuum_sim/config/vacuum_navigate.xml
controller_server:
  ros__parameters:
    controller_frequency: 20.0
    costmap_update_timeout: 0.3
    min_x_velocity_threshold: 0.001
    min_y_velocity_threshold: 0.5
    min_theta_velocity_threshold: 0.001
    failure_tolerance: 0.3
    progress_checker_plugins:
    - progress_checker
    goal_checker_plugins:
    - general_goal_checker
    controller_plugins:
    - FollowPath
    use_realtime_priority: false
    progress_checker:
      plugin: nav2_controller::SimpleProgressChecker
      required_movement_radius: 0.15
      movement_time_allowance: 30.0
    general_goal_checker:
      stateful: true
      plugin: nav2_controller::SimpleGoalChecker
      xy_goal_tolerance: 0.1
      yaw_goal_tolerance: 0.2
    FollowPath:
      plugin: dwb_core::DWBLocalPlanner
      debug_trajectory_details: false
      min_vel_x: 0.0
      max_vel_x: 0.2
      min_vel_y: 0.0
      max_vel_y: 0.0
      max_vel_theta: 0.7
      min_speed_xy: 0.0
      max_speed_xy: 0.2
      min_speed_theta: 0.0
      acc_lim_x: 0.3
      acc_lim_y: 0.0
      acc_lim_theta: 1.0
      decel_lim_x: -0.3
      decel_lim_y: 0.0
      decel_lim_theta: -1.0
      vx_samples: 20
      vy_samples: 1
      vtheta_samples: 20
      sim_time: 1.7
      linear_granularity: 0.05
      angular_granularity: 0.025
      transform_tolerance: 0.2
      xy_goal_tolerance: 0.1
      trans_stopped_velocity: 0.02
      short_circuit_trajectory_evaluation: true
      stateful: true
      critics:
      - RotateToGoal
      - Oscillation
      - ObstacleFootprint
      - GoalAlign
      - PathAlign
      - PathDist
      - GoalDist
      PathAlign.scale: 32.0
      PathAlign.forward_point_distance: 0.1
      GoalAlign.scale: 24.0
      GoalAlign.forward_point_distance: 0.1
      PathDist.scale: 32.0
      GoalDist.scale: 24.0
      RotateToGoal.scale: 32.0
      RotateToGoal.slowing_factor: 5.0
      RotateToGoal.lookahead_time: -1.0
      ObstacleFootprint.scale: 1.0
    use_sim_time: true
    odom_topic: /odom
    enable_stamped_cmd_vel: false
local_costmap:
  local_costmap:
    ros__parameters:
      update_frequency: 5.0
      publish_frequency: 2.0
      global_frame: odom
      robot_base_frame: base_footprint
      rolling_window: true
      width: 3
      height: 3
      resolution: 0.05
      plugins:
      - obstacle_layer
      - inflation_layer
      inflation_layer:
        plugin: nav2_costmap_2d::InflationLayer
        cost_scaling_factor: 4.0
        inflation_radius: 0.5
      static_layer:
        plugin: nav2_costmap_2d::StaticLayer
        map_subscribe_transient_local: true
      always_send_full_costmap: true
      use_sim_time: true
      footprint: '[[0.120726, 0.0], [0.11783, 0.029405], [0.109252, 0.05768], [0.095324,
        0.083739], [0.076579, 0.106579], [0.053739, 0.125324], [0.02768, 0.139252],
        [-0.000595, 0.14783], [-0.03, 0.150726], [-0.059405, 0.14783], [-0.08768,
        0.139252], [-0.113739, 0.125324], [-0.136579, 0.106579], [-0.155324, 0.083739],
        [-0.169252, 0.05768], [-0.17783, 0.029405], [-0.180726, 0.0], [-0.17783, -0.029405],
        [-0.169252, -0.05768], [-0.155324, -0.083739], [-0.136579, -0.106579], [-0.113739,
        -0.125324], [-0.08768, -0.139252], [-0.059405, -0.14783], [-0.03, -0.150726],
        [-0.000595, -0.14783], [0.02768, -0.139252], [0.053739, -0.125324], [0.076579,
        -0.106579], [0.095324, -0.083739], [0.109252, -0.05768], [0.11783, -0.029405]]'
      footprint_padding: 0.02
      obstacle_layer:
        plugin: nav2_costmap_2d::ObstacleLayer
        enabled: true
        max_obstacle_height: 2.0
        observation_sources: scan
        scan:
          topic: /scan
          max_obstacle_height: 2.0
          clearing: true
          marking: true
          data_type: LaserScan
          raytrace_max_range: 8.0
          raytrace_min_range: 0.0
          obstacle_max_range: 6.0
          obstacle_min_range: 0.0
global_costmap:
  global_costmap:
    ros__parameters:
      update_frequency: 1.0
      publish_frequency: 1.0
      global_frame: map
      robot_base_frame: base_footprint
      resolution: 0.05
      track_unknown_space: true
      plugins:
      - static_layer
      - obstacle_layer
      - inflation_layer
      obstacle_layer:
        plugin: nav2_costmap_2d::ObstacleLayer
        enabled: true
        observation_sources: scan
        scan:
          topic: /scan
          max_obstacle_height: 2.0
          clearing: true
          marking: true
          data_type: LaserScan
          raytrace_max_range: 8.0
          raytrace_min_range: 0.0
          obstacle_max_range: 6.0
          obstacle_min_range: 0.0
      static_layer:
        plugin: nav2_costmap_2d::StaticLayer
        map_subscribe_transient_local: true
      inflation_layer:
        plugin: nav2_costmap_2d::InflationLayer
        cost_scaling_factor: 4.0
        inflation_radius: 0.5
      always_send_full_costmap: true
      use_sim_time: true
      footprint: '[[0.120726, 0.0], [0.11783, 0.029405], [0.109252, 0.05768], [0.095324,
        0.083739], [0.076579, 0.106579], [0.053739, 0.125324], [0.02768, 0.139252],
        [-0.000595, 0.14783], [-0.03, 0.150726], [-0.059405, 0.14783], [-0.08768,
        0.139252], [-0.113739, 0.125324], [-0.136579, 0.106579], [-0.155324, 0.083739],
        [-0.169252, 0.05768], [-0.17783, 0.029405], [-0.180726, 0.0], [-0.17783, -0.029405],
        [-0.169252, -0.05768], [-0.155324, -0.083739], [-0.136579, -0.106579], [-0.113739,
        -0.125324], [-0.08768, -0.139252], [-0.059405, -0.14783], [-0.03, -0.150726],
        [-0.000595, -0.14783], [0.02768, -0.139252], [0.053739, -0.125324], [0.076579,
        -0.106579], [0.095324, -0.083739], [0.109252, -0.05768], [0.11783, -0.029405]]'
      footprint_padding: 0.02
map_saver:
  ros__parameters:
    save_map_timeout: 5.0
    free_thresh_default: 0.25
    occupied_thresh_default: 0.65
    map_subscribe_transient_local: true
    use_sim_time: true
planner_server:
  ros__parameters:
    expected_planner_frequency: 20.0
    planner_plugins:
    - GridBased
    costmap_update_timeout: 1.0
    GridBased:
      plugin: nav2_navfn_planner::NavfnPlanner
      tolerance: 0.1
      use_astar: true
      allow_unknown: false
    use_sim_time: true
smoother_server:
  ros__parameters:
    smoother_plugins:
    - simple_smoother
    simple_smoother:
      plugin: nav2_smoother::SimpleSmoother
      tolerance: 1.0e-10
      max_its: 1000
      do_refinement: true
    use_sim_time: true
behavior_server:
  ros__parameters:
    local_costmap_topic: local_costmap/costmap_raw
    global_costmap_topic: global_costmap/costmap_raw
    local_footprint_topic: local_costmap/published_footprint
    global_footprint_topic: global_costmap/published_footprint
    cycle_frequency: 10.0
    behavior_plugins:
    - wait
    spin:
      plugin: nav2_behaviors::Spin
    backup:
      plugin: nav2_behaviors::BackUp
    drive_on_heading:
      plugin: nav2_behaviors::DriveOnHeading
    wait:
      plugin: nav2_behaviors::Wait
    assisted_teleop:
      plugin: nav2_behaviors::AssistedTeleop
    local_frame: odom
    global_frame: map
    robot_base_frame: base_footprint
    transform_tolerance: 0.1
    simulate_ahead_time: 2.0
    max_rotational_vel: 1.0
    min_rotational_vel: 0.4
    rotational_acc_lim: 3.2
    use_sim_time: true
    odom_topic: /odom
    enable_stamped_cmd_vel: false
waypoint_follower:
  ros__parameters:
    loop_rate: 20
    stop_on_failure: false
    action_server_result_timeout: 900.0
    waypoint_task_executor_plugin: wait_at_waypoint
    wait_at_waypoint:
      plugin: nav2_waypoint_follower::WaitAtWaypoint
      enabled: true
      waypoint_pause_duration: 200
    use_sim_time: true
route_server:
  ros__parameters:
    boundary_radius_to_achieve_node: 1.0
    radius_to_achieve_node: 2.0
    smooth_corners: true
    operations:
    - AdjustSpeedLimit
    - ReroutingService
    - CollisionMonitor
    ReroutingService:
      plugin: nav2_route::ReroutingService
    AdjustSpeedLimit:
      plugin: nav2_route::AdjustSpeedLimit
    CollisionMonitor:
      plugin: nav2_route::CollisionMonitor
      max_collision_dist: 3.0
    edge_cost_functions:
    - DistanceScorer
    - CostmapScorer
    DistanceScorer:
      plugin: nav2_route::DistanceScorer
    CostmapScorer:
      plugin: nav2_route::CostmapScorer
    use_sim_time: true
velocity_smoother:
  ros__parameters:
    smoothing_frequency: 20.0
    stamp_smoothed_velocity_with_smoothing_time: false
    scale_velocities: false
    feedback: OPEN_LOOP
    max_velocity:
    - 0.2
    - 0.0
    - 0.7
    min_velocity:
    - 0.0
    - 0.0
    - -0.7
    max_accel:
    - 0.3
    - 0.0
    - 1.0
    max_decel:
    - -0.3
    - 0.0
    - -1.0
    odom_topic: /odom
    odom_duration: 0.1
    deadband_velocity:
    - 0.0
    - 0.0
    - 0.0
    velocity_timeout: 0.5
    use_sim_time: true
    enable_stamped_cmd_vel: false
collision_monitor:
  ros__parameters:
    base_frame_id: base_footprint
    odom_frame_id: odom
    cmd_vel_in_topic: /vacuum/selected_cmd_vel
    cmd_vel_out_topic: cmd_vel
    state_topic: collision_monitor_state
    transform_tolerance: 0.2
    source_timeout: 0.5
    base_shift_correction: true
    stop_pub_timeout: 2.0
    polygons:
    - StopZone
    - SlowZone
    - FootprintApproach
    FootprintApproach:
      type: polygon
      action_type: approach
      footprint_topic: /local_costmap/published_footprint
      time_before_collision: 0.55
      simulation_time_step: 0.02
      min_points: 1
      visualize: false
      enabled: true
    observation_sources:
    - scan
    scan:
      type: scan
      topic: scan
      min_height: 0.0
      max_height: 2.0
      enabled: true
      source_timeout: 0.5
    use_sim_time: true
    enable_stamped_cmd_vel: false
    StopZone:
      type: velocity_polygon
      action_type: stop
      min_points: 1
      visualize: true
      polygon_pub_topic: vacuum_stopzone
      enabled: true
      holonomic: false
      velocity_polygons:
      - forward
      - reverse
      - rotation
      forward:
        points: '[[-0.03, 0.2], [-0.03, -0.2], [0.62, -0.2], [0.62, 0.2]]'
        linear_min: 0.001
        linear_max: 2.0
        theta_min: -3.0
        theta_max: 3.0
      reverse:
        points: '[[-0.6, 0.2], [-0.6, -0.2], [-0.03, -0.2], [-0.03, 0.2]]'
        linear_min: -2.0
        linear_max: -0.001
        theta_min: -3.0
        theta_max: 3.0
      rotation:
        points: '[[0.170968, 0.0], [0.167106, 0.039207], [0.15567, 0.076907], [0.137099,
          0.111652], [0.112106, 0.142106], [0.081652, 0.167099], [0.046907, 0.18567],
          [0.009207, 0.197106], [-0.03, 0.200968], [-0.069207, 0.197106], [-0.106907,
          0.18567], [-0.141652, 0.167099], [-0.172106, 0.142106], [-0.197099, 0.111652],
          [-0.21567, 0.076907], [-0.227106, 0.039207], [-0.230968, 0.0], [-0.227106,
          -0.039207], [-0.21567, -0.076907], [-0.197099, -0.111652], [-0.172106, -0.142106],
          [-0.141652, -0.167099], [-0.106907, -0.18567], [-0.069207, -0.197106], [-0.03,
          -0.200968], [0.009207, -0.197106], [0.046907, -0.18567], [0.081652, -0.167099],
          [0.112106, -0.142106], [0.137099, -0.111652], [0.15567, -0.076907], [0.167106,
          -0.039207]]'
        linear_min: -2.0
        linear_max: 2.0
        theta_min: -3.0
        theta_max: 3.0
    SlowZone:
      type: velocity_polygon
      action_type: slowdown
      min_points: 1
      visualize: true
      polygon_pub_topic: vacuum_slowzone
      enabled: true
      holonomic: false
      velocity_polygons:
      - forward
      - reverse
      - rotation
      slowdown_ratio: 0.4
      forward:
        points: '[[-0.03, 0.25], [-0.03, -0.25], [1.7, -0.25], [1.7, 0.25]]'
        linear_min: 0.001
        linear_max: 2.0
        theta_min: -3.0
        theta_max: 3.0
      reverse:
        points: '[[-1.2, 0.25], [-1.2, -0.25], [-0.03, -0.25], [-0.03, 0.25]]'
        linear_min: -2.0
        linear_max: -0.001
        theta_min: -3.0
        theta_max: 3.0
      rotation:
        points: '[[0.251355, 0.0], [0.245949, 0.05489], [0.229938, 0.10767], [0.203938,
          0.156312], [0.168948, 0.198948], [0.126312, 0.233938], [0.07767, 0.259938],
          [0.02489, 0.275949], [-0.03, 0.281355], [-0.08489, 0.275949], [-0.13767,
          0.259938], [-0.186312, 0.233938], [-0.228948, 0.198948], [-0.263938, 0.156312],
          [-0.289938, 0.10767], [-0.305949, 0.05489], [-0.311355, 0.0], [-0.305949,
          -0.05489], [-0.289938, -0.10767], [-0.263938, -0.156312], [-0.228948, -0.198948],
          [-0.186312, -0.233938], [-0.13767, -0.259938], [-0.08489, -0.275949], [-0.03,
          -0.281355], [0.02489, -0.275949], [0.07767, -0.259938], [0.126312, -0.233938],
          [0.168948, -0.198948], [0.203938, -0.156312], [0.229938, -0.10767], [0.245949,
          -0.05489]]'
        linear_min: -2.0
        linear_max: 2.0
        theta_min: -3.0
        theta_max: 3.0
docking_server:
  ros__parameters:
    controller_frequency: 50.0
    initial_perception_timeout: 5.0
    wait_charge_timeout: 5.0
    dock_approach_timeout: 30.0
    undock_linear_tolerance: 0.05
    undock_angular_tolerance: 0.1
    max_retries: 3
    base_frame: base_footprint
    fixed_frame: odom
    dock_backwards: false
    dock_prestaging_tolerance: 0.5
    dock_plugins:
    - simple_charging_dock
    simple_charging_dock:
      plugin: opennav_docking::SimpleChargingDock
      docking_threshold: 0.05
      staging_x_offset: -0.7
      use_external_detection_pose: true
      use_battery_status: false
      use_stall_detection: false
      external_detection_timeout: 1.0
      external_detection_translation_x: -0.18
      external_detection_translation_y: 0.0
      external_detection_rotation_roll: -1.57
      external_detection_rotation_pitch: -1.57
      external_detection_rotation_yaw: 0.0
      filter_coef: 0.1
    controller:
      k_phi: 3.0
      k_delta: 2.0
      v_linear_min: 0.15
      v_linear_max: 0.15
      use_collision_detection: true
      costmap_topic: local_costmap/costmap_raw
      footprint_topic: local_costmap/published_footprint
      transform_tolerance: 0.1
      projection_time: 5.0
      simulation_step: 0.1
      dock_collision_threshold: 0.3
    use_sim_time: true
    enable_stamped_cmd_vel: false
loopback_simulator:
  ros__parameters:
    base_frame_id: base_footprint
    odom_frame_id: odom
    map_frame_id: map
    scan_frame_id: base_scan
    update_duration: 0.02
    scan_range_min: 0.05
    scan_range_max: 30.0
    scan_angle_min: -3.1415
    scan_angle_max: 3.1415
    scan_angle_increment: 0.02617
    scan_use_inf: true
    use_sim_time: true


## src/vacuum_sim/config/robot-profile.json

{
  "version": 2,
  "scope": "simulation",
  "hardware": {
    "drive_motors": "2 x NEMA 17, mounted beneath the chassis",
    "stepper_drivers": "2 x TB6600 modules",
    "microcontroller": "Arduino Mega 2560",
    "computer": "Orange Pi 5",
    "lidar": "RPLIDAR C1",
    "wheel_diameter_m": 0.07,
    "wheel_separation_m": 0.22,
    "chassis_diameter_m": 0.3,
    "motor_body_m": [
      0.0423,
      0.04,
      0.0423
    ],
    "estimated_geometry": "Motor length, driver enclosure, mount height, mass and chassis layout are provisional; exact motor/driver variants were not supplied."
  },
  "drive": {
    "forward_m_s": 1.5,
    "reverse_m_s": 0.9,
    "turn_rad_s": 2.4,
    "acceleration_m_s2": 6.0,
    "angular_acceleration_rad_s2": 14.0,
    "input_period_s": 0.02,
    "odometry_window_samples": 3,
    "require_hold_button": false
  },
  "room": {
    "width_m": 16.0,
    "depth_m": 12.0
  },
  "lidar": {
    "min_range_m": 0.05,
    "max_range_m": 12.0,
    "scan_hz": 10.0,
    "samples": 500,
    "serial_baud": 460800
  }
}


## src/vacuum_sim/config/controllers.yaml

controller_manager:
  ros__parameters:
    update_rate: 60
    use_sim_time: true
    joint_state_broadcaster:
      type: joint_state_broadcaster/JointStateBroadcaster
    diff_drive_controller:
      type: diff_drive_controller/DiffDriveController
diff_drive_controller:
  ros__parameters:
    use_sim_time: true
    left_wheel_names:
    - left_wheel_joint
    right_wheel_names:
    - right_wheel_joint
    wheel_separation: 0.22
    wheel_radius: 0.035
    publish_rate: 60.0
    odom_frame_id: odom
    base_frame_id: base_footprint
    enable_odom_tf: true
    open_loop: false
    position_feedback: true
    cmd_vel_timeout: 0.25
    pose_covariance_diagonal:
    - 0.001
    - 0.001
    - 0.001
    - 0.001
    - 0.001
    - 0.01
    twist_covariance_diagonal:
    - 0.001
    - 0.001
    - 0.001
    - 0.001
    - 0.001
    - 0.01
    linear.x.has_velocity_limits: true
    linear.x.max_velocity: 1.5
    linear.x.min_velocity: -0.9
    linear.x.has_acceleration_limits: true
    linear.x.max_acceleration: 6.0
    linear.x.min_acceleration: -6.0
    angular.z.has_velocity_limits: true
    angular.z.max_velocity: 2.4
    angular.z.min_velocity: -2.4
    angular.z.has_acceleration_limits: true
    angular.z.max_acceleration: 14.0
    angular.z.min_acceleration: -14.0
    velocity_rolling_window_size: 3
    linear.x.has_jerk_limits: false
    angular.z.has_jerk_limits: false


## src/vacuum_sim/launch

## src/vacuum_sim/launch/mapping.launch.py

from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    slam = Path(get_package_share_directory('slam_toolbox'))
    return LaunchDescription([IncludeLaunchDescription(
        PythonLaunchDescriptionSource(str(slam / 'launch/online_async_launch.py')),
        launch_arguments={'use_sim_time': 'true', 'slam_params_file': str(package / 'config/slam.yaml')}.items())])


## src/vacuum_sim/launch/navigation.launch.py

"""Local destination navigation, with only the servers used by this robot's BT."""
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    params = LaunchConfiguration('params_file')
    servers = [
        ('nav2_controller', 'controller_server', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_planner', 'planner_server', []),
        ('nav2_behaviors', 'behavior_server', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_velocity_smoother', 'velocity_smoother', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_collision_monitor', 'collision_monitor', []),
        ('nav2_bt_navigator', 'bt_navigator', []),
    ]
    actions = [DeclareLaunchArgument('params_file', default_value=str(package / 'config/vacuum_nav2.yaml'))]
    for pkg, name, remap in servers:
        actions.append(Node(package=pkg, executable=name, name=name,
                            parameters=[params, {'use_sim_time': True}],
                            remappings=[('/tf','tf'),('/tf_static','tf_static')] + remap,
                            output='screen'))
    # Allow process/plugin startup and local discovery before lifecycle requests.
    # All commands still pass through the gate and Collision Monitor.
    actions.append(TimerAction(period=4., actions=[Node(
        package='nav2_lifecycle_manager', executable='lifecycle_manager',
        name='lifecycle_manager_navigation', output='screen',
        parameters=[{'use_sim_time': True, 'autostart': True,
                     'node_names': [name for _, name, _ in servers],
                     'bond_timeout': 4.0}])]))
    return LaunchDescription(actions)


## src/vacuum_sim/launch/navigation.launch.py.before-autonomy-20261006

## src/vacuum_sim/launch/sim.launch.py

from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, RegisterEventHandler, SetEnvironmentVariable, ExecuteProcess
from launch.conditions import IfCondition
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    gz_launch = str(Path(get_package_share_directory('ros_gz_sim')) / 'launch' / 'gz_sim.launch.py')
    description = ParameterValue(Command(['xacro ', str(package / 'urdf/vacuum.urdf.xacro'), ' camera_width:=', LaunchConfiguration('camera_width'), ' camera_height:=', LaunchConfiguration('camera_height'), ' camera_rate:=', LaunchConfiguration('camera_rate')]), value_type=str)
    spawn = Node(package='ros_gz_sim', executable='create', arguments=[
        '-world', 'vacuum_room', '-name', 'vacuum', '-topic', '/robot_description', '-z', '0.015'], output='screen')
    controllers = Node(package='controller_manager', executable='spawner', arguments=[
        'joint_state_broadcaster', 'diff_drive_controller', '--controller-manager-timeout', '120'], output='screen')
    return LaunchDescription([
        DeclareLaunchArgument('camera_width', default_value='320'),
        DeclareLaunchArgument('camera_height', default_value='240'),
        DeclareLaunchArgument('camera_rate', default_value='60'),
        DeclareLaunchArgument('gui', default_value='true'),
        DeclareLaunchArgument('rviz', default_value='true'),
        DeclareLaunchArgument('rviz_config', default_value=str(package / 'config/view.rviz')),
        SetEnvironmentVariable('ROS_AUTOMATIC_DISCOVERY_RANGE', 'LOCALHOST'),
        SetEnvironmentVariable('ROS_DOMAIN_ID', '42'),
        SetEnvironmentVariable('GZ_PARTITION', 'vacuum_sim_42'),
        SetEnvironmentVariable('GZ_IP', '127.0.0.1'),
        # Direct argv keeps Gazebo under launch's signal handling; a shell wrapper
        # previously exited first and left its Gazebo child running.
        ExecuteProcess(cmd=['gz', 'sim', '-r', '-s', '-v', '2', str(package / 'worlds/room.sdf')], output='screen'),
        ExecuteProcess(cmd=['gz', 'sim', '-g', '-v', '2'], output='screen', condition=IfCondition(LaunchConfiguration('gui'))),
        Node(package='robot_state_publisher', executable='robot_state_publisher',
             parameters=[{'robot_description': description, 'use_sim_time': True}], output='screen'),
        Node(package='ros_gz_bridge', executable='parameter_bridge', parameters=[
            {'config_file': str(package / 'config/bridge.yaml'), 'use_sim_time': True}], output='screen'),
        RegisterEventHandler(OnProcessExit(target_action=spawn, on_exit=[controllers])),
        spawn,
        Node(package='vacuum_sim', executable='twist_adapter.py', parameters=[{'use_sim_time': True}], output='screen'),
        Node(package='rviz2', executable='rviz2', arguments=['-d', LaunchConfiguration('rviz_config')],
             parameters=[{'use_sim_time': True}], condition=IfCondition(LaunchConfiguration('rviz')), output='screen'),
    ])


## src/vacuum_sim/worlds

## src/vacuum_sim/worlds/room.sdf

<sdf version="1.9">
  <world name="vacuum_room">
    <physics name="physics" type="ignored">
      <max_step_size>0.005555555555555556</max_step_size>
      <real_time_factor>1.0</real_time_factor>
    </physics>
    <gravity>0 0 -9.81</gravity>
    <plugin filename="gz-sim-physics-system" name="gz::sim::systems::Physics" />
    <plugin filename="gz-sim-user-commands-system" name="gz::sim::systems::UserCommands" />
    <plugin filename="gz-sim-scene-broadcaster-system" name="gz::sim::systems::SceneBroadcaster" />
    <plugin filename="gz-sim-sensors-system" name="gz::sim::systems::Sensors">
      <render_engine>ogre2</render_engine>
    </plugin>
    <scene>
      <ambient>.7 .7 .7 1</ambient>
      <background>.69 .79 .85 1</background>
      <shadows>false</shadows>
    </scene>
    <light name="afternoon_daylight" type="directional">
      <pose>0 0 6 0 0 0</pose>
      <diffuse>.75 .72 .65 1</diffuse>
      <specular>.15 .15 .15 1</specular>
      <direction>-.5 -.4 -1</direction>
      <cast_shadows>false</cast_shadows>
    </light>
    <light name="soft_window_fill" type="directional">
      <pose>0 0 6 0 0 0</pose>
      <diffuse>.25 .28 .3 1</diffuse>
      <specular>0 0 0 1</specular>
      <direction>.4 .4 -1</direction>
      <cast_shadows>false</cast_shadows>
    </light>
    <gui fullscreen="false">
      <camera name="user_camera">
        <pose>13 -16 13 0 .62 2.2</pose>
      </camera>
    </gui>
    <model name="furnished_living_room">
      <static>true</static>
      <self_collide>false</self_collide>
      <link name="room">
        <collision name="architecture_proxy0">
          <pose>0.0 0.0 -0.04 0 0 0</pose>
          <geometry>
            <box>
              <size>16.4 12.342857142857143 0.08</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy1">
          <pose>0.0 -6.0 1.4 0 0 0</pose>
          <geometry>
            <box>
              <size>16.4 0.2057142857142857 2.8</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy2">
          <pose>-8.0 0.0 1.4 0 0 0</pose>
          <geometry>
            <box>
              <size>0.24 12.0 2.8</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy3">
          <pose>8.0 0.0 1.4 0 0 0</pose>
          <geometry>
            <box>
              <size>0.24 12.0 2.8</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy4">
          <pose>0.0 6.0 0.45 0 0 0</pose>
          <geometry>
            <box>
              <size>16.4 0.2057142857142857 0.9</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy5">
          <pose>0.0 6.0 2.65 0 0 0</pose>
          <geometry>
            <box>
              <size>16.4 0.2057142857142857 0.3</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy6">
          <pose>-6.3 6.0 1.7 0 0 0</pose>
          <geometry>
            <box>
              <size>3.8 0.2057142857142857 1.6</size>
            </box>
          </geometry>
        </collision>
        <collision name="architecture_proxy7">
          <pose>6.3 6.0 1.7 0 0 0</pose>
          <geometry>
            <box>
              <size>3.8 0.2057142857142857 1.6</size>
            </box>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy0">
          <pose>-2.8 4.95 0.28 0 0 0</pose>
          <geometry>
            <box>
              <size>2.55 0.9 0.3</size>
            </box>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy1">
          <pose>-2.8 5.3100000000000005 0.65 0 0 0</pose>
          <geometry>
            <box>
              <size>2.55 0.21 0.75</size>
            </box>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy2">
          <pose>-4.01 4.92 0.53 0 0 0</pose>
          <geometry>
            <box>
              <size>0.18 0.87 0.56</size>
            </box>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy3">
          <pose>-1.5899999999999999 4.92 0.53 0 0 0</pose>
          <geometry>
            <box>
              <size>0.18 0.87 0.56</size>
            </box>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy4">
          <pose>-3.88 4.65 0.09 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.18</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy5">
          <pose>-1.7199999999999998 4.65 0.09 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.18</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy6">
          <pose>-3.88 5.25 0.09 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.18</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="three_seat_sofa_proxy7">
          <pose>-1.7199999999999998 5.25 0.09 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.18</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="rounded_coffee_table_proxy0">
          <pose>-2.8 3.65 0.4 0 0 0</pose>
          <geometry>
            <box>
              <size>1.25 0.63 0.07</size>
            </box>
          </geometry>
        </collision>
        <collision name="rounded_coffee_table_proxy1">
          <pose>-3.2699999999999996 3.44 0.2 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.4</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="rounded_coffee_table_proxy2">
          <pose>-3.2699999999999996 3.86 0.2 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.4</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="rounded_coffee_table_proxy3">
          <pose>-2.33 3.44 0.2 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.4</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="rounded_coffee_table_proxy4">
          <pose>-2.33 3.86 0.2 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.4</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="oak_media_console_proxy0">
          <pose>7.55 3.3 0.35 0 0 0</pose>
          <geometry>
            <box>
              <size>0.45 2.05 0.51</size>
            </box>
          </geometry>
        </collision>
        <collision name="oak_media_console_proxy1">
          <pose>7.55 2.48 0.075 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.15</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="oak_media_console_proxy2">
          <pose>7.55 4.12 0.075 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.035</radius>
              <length>0.15</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="bookcase_proxy0">
          <pose>-7.57 3.4 0.105 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.21</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy1">
          <pose>-7.7 3.4 1.05 0 0 0</pose>
          <geometry>
            <box>
              <size>0.12 1.2 2.1</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy2">
          <pose>-7.57 2.83 1.05 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 0.045 2.1</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy3">
          <pose>-7.57 3.9699999999999998 1.05 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 0.045 2.1</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy4">
          <pose>-7.57 3.4 0.06 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy5">
          <pose>-7.57 3.4 0.5 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy6">
          <pose>-7.57 3.4 0.96 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy7">
          <pose>-7.57 3.4 1.42 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy8">
          <pose>-7.57 3.4 1.88 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="bookcase_proxy9">
          <pose>-7.57 3.4 2.12 0 0 0</pose>
          <geometry>
            <box>
              <size>0.42 1.2 0.035</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_table_proxy0">
          <pose>-4.2 -2.0 0.76 0 0 0</pose>
          <geometry>
            <box>
              <size>1.45 0.88 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_table_proxy1">
          <pose>-4.78 -2.3 0.37 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.045</radius>
              <length>0.74</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_table_proxy2">
          <pose>-4.78 -1.7 0.37 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.045</radius>
              <length>0.74</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_table_proxy3">
          <pose>-3.62 -2.3 0.37 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.045</radius>
              <length>0.74</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_table_proxy4">
          <pose>-3.62 -1.7 0.37 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.045</radius>
              <length>0.74</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy0">
          <pose>-4.2 -1.23 0.45 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy1">
          <pose>-4.2 -1.425 0.72 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy2">
          <pose>-4.04 -1.07 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy3">
          <pose>-4.04 -1.3900000000000001 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy4">
          <pose>-4.36 -1.0699999999999998 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_north_proxy5">
          <pose>-4.36 -1.39 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy0">
          <pose>-4.2 -2.78 0.45 0 0 0</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy1">
          <pose>-4.2 -2.585 0.72 0 0 0</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy2">
          <pose>-4.36 -2.94 0.225 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy3">
          <pose>-4.36 -2.6199999999999997 0.225 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy4">
          <pose>-4.04 -2.94 0.225 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_south_proxy5">
          <pose>-4.04 -2.6199999999999997 0.225 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy0">
          <pose>-5.27 -2.0 0.45 0 0 -1.5707963267948966</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy1">
          <pose>-5.074999999999999 -2.0 0.72 0 0 -1.5707963267948966</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy2">
          <pose>-5.43 -1.84 0.225 0 0 -1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy3">
          <pose>-5.109999999999999 -1.84 0.225 0 0 -1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy4">
          <pose>-5.43 -2.16 0.225 0 0 -1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_west_proxy5">
          <pose>-5.109999999999999 -2.16 0.225 0 0 -1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_east_proxy0">
          <pose>-3.13 -2.0 0.45 0 0 1.5707963267948966</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_east_proxy1">
          <pose>-3.3249999999999997 -2.0 0.72 0 0 1.5707963267948966</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="dining_chair_east_proxy2">
          <pose>-2.9699999999999998 -2.16 0.225 0 0 1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_east_proxy3">
          <pose>-3.29 -2.16 0.225 0 0 1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_east_proxy4">
          <pose>-2.9699999999999998 -1.84 0.225 0 0 1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="dining_chair_east_proxy5">
          <pose>-3.29 -1.84 0.225 0 0 1.5707963267948966</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="home_office_desk_proxy0">
          <pose>5.7 -5.55 0.76 0 0 0</pose>
          <geometry>
            <box>
              <size>1.65 0.65 0.055</size>
            </box>
          </geometry>
        </collision>
        <collision name="home_office_desk_proxy1">
          <pose>5.0 -5.78 0.37 0 0 0</pose>
          <geometry>
            <box>
              <size>0.045 0.045 0.74</size>
            </box>
          </geometry>
        </collision>
        <collision name="home_office_desk_proxy2">
          <pose>5.0 -5.319999999999999 0.37 0 0 0</pose>
          <geometry>
            <box>
              <size>0.045 0.045 0.74</size>
            </box>
          </geometry>
        </collision>
        <collision name="home_office_desk_proxy3">
          <pose>6.4 -5.78 0.37 0 0 0</pose>
          <geometry>
            <box>
              <size>0.045 0.045 0.74</size>
            </box>
          </geometry>
        </collision>
        <collision name="home_office_desk_proxy4">
          <pose>6.4 -5.319999999999999 0.37 0 0 0</pose>
          <geometry>
            <box>
              <size>0.045 0.045 0.74</size>
            </box>
          </geometry>
        </collision>
        <collision name="office_chair_proxy0">
          <pose>5.7 -4.65 0.45 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="office_chair_proxy1">
          <pose>5.7 -4.845000000000001 0.72 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="office_chair_proxy2">
          <pose>5.86 -4.49 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="office_chair_proxy3">
          <pose>5.86 -4.8100000000000005 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="office_chair_proxy4">
          <pose>5.54 -4.49 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="office_chair_proxy5">
          <pose>5.54 -4.8100000000000005 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="floor_lamp_proxy0">
          <pose>-0.9 4.95 0.105 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.2</radius>
              <length>0.21</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="floor_lamp_proxy1">
          <pose>-0.9 4.95 0.77 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.018</radius>
              <length>1.5</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="window_plant_proxy0">
          <pose>5.8 5.3 0.18 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.22</radius>
              <length>0.36</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="entry_plant_proxy0">
          <pose>-7.0 -5.25 0.18 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.22</radius>
              <length>0.36</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="kitchen_wall_proxy0">
          <pose>-2.0 -5.65 0.46 0 0 0</pose>
          <geometry>
            <box>
              <size>0.98 0.6 0.92</size>
            </box>
          </geometry>
        </collision>
        <collision name="kitchen_wall_proxy1">
          <pose>-1.0 -5.65 0.46 0 0 0</pose>
          <geometry>
            <box>
              <size>0.98 0.6 0.92</size>
            </box>
          </geometry>
        </collision>
        <collision name="kitchen_wall_proxy2">
          <pose>0.0 -5.65 0.46 0 0 0</pose>
          <geometry>
            <box>
              <size>0.98 0.6 0.92</size>
            </box>
          </geometry>
        </collision>
        <collision name="kitchen_wall_proxy3">
          <pose>1.0 -5.65 0.46 0 0 0</pose>
          <geometry>
            <box>
              <size>0.98 0.6 0.92</size>
            </box>
          </geometry>
        </collision>
        <collision name="kitchen_wall_proxy4">
          <pose>2.0 -5.65 0.46 0 0 0</pose>
          <geometry>
            <box>
              <size>0.98 0.6 0.92</size>
            </box>
          </geometry>
        </collision>
        <collision name="kitchen_wall_proxy5">
          <pose>0.0 -5.65 0.95 0 0 0</pose>
          <geometry>
            <box>
              <size>5.1 0.65 0.055</size>
            </box>
          </geometry>
        </collision>
        <collision name="kitchen_island_proxy0">
          <pose>1.3 -2.7 0.45 0 0 0</pose>
          <geometry>
            <box>
              <size>1.9 0.75 0.9</size>
            </box>
          </geometry>
        </collision>
        <collision name="kitchen_island_proxy1">
          <pose>1.3 -2.7 0.93 0 0 0</pose>
          <geometry>
            <box>
              <size>2.1 0.95 0.055</size>
            </box>
          </geometry>
        </collision>
        <collision name="island_stool_left_proxy0">
          <pose>0.75 -1.75 0.45 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="island_stool_left_proxy1">
          <pose>0.75 -1.945 0.72 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="island_stool_left_proxy2">
          <pose>0.91 -1.59 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="island_stool_left_proxy3">
          <pose>0.9099999999999999 -1.9100000000000001 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="island_stool_left_proxy4">
          <pose>0.5900000000000001 -1.5899999999999999 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="island_stool_left_proxy5">
          <pose>0.59 -1.91 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="island_stool_right_proxy0">
          <pose>1.9 -1.75 0.45 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.45 0.45 0.065</size>
            </box>
          </geometry>
        </collision>
        <collision name="island_stool_right_proxy1">
          <pose>1.9 -1.945 0.72 0 0 3.141592653589793</pose>
          <geometry>
            <box>
              <size>0.46 0.065 0.5</size>
            </box>
          </geometry>
        </collision>
        <collision name="island_stool_right_proxy2">
          <pose>2.06 -1.59 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="island_stool_right_proxy3">
          <pose>2.06 -1.9100000000000001 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="island_stool_right_proxy4">
          <pose>1.74 -1.5899999999999999 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="island_stool_right_proxy5">
          <pose>1.7399999999999998 -1.91 0.225 0 0 3.141592653589793</pose>
          <geometry>
            <cylinder>
              <radius>0.025</radius>
              <length>0.45</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="reading_lounge_proxy0">
          <pose>4.6 2.8 0.26 0 0 -0.35</pose>
          <geometry>
            <box>
              <size>1.1 0.87 0.33</size>
            </box>
          </geometry>
        </collision>
        <collision name="reading_lounge_proxy1">
          <pose>4.709727298385744 3.100599268111161 0.65 0 0 -0.35</pose>
          <geometry>
            <box>
              <size>1.1 0.2 0.62</size>
            </box>
          </geometry>
        </collision>
        <collision name="reading_lounge_proxy2">
          <pose>4.139707370704784 2.968019925653171 0.5 0 0 -0.35</pose>
          <geometry>
            <box>
              <size>0.14 0.8 0.4</size>
            </box>
          </geometry>
        </collision>
        <collision name="reading_lounge_proxy3">
          <pose>5.0602926292952155 2.6319800743468287 0.5 0 0 -0.35</pose>
          <geometry>
            <box>
              <size>0.14 0.8 0.4</size>
            </box>
          </geometry>
        </collision>
        <collision name="reading_lounge_proxy4">
          <pose>4.102594118367465 2.6622052652770756 0.065 0 0 -0.35</pose>
          <geometry>
            <cylinder>
              <radius>0.027</radius>
              <length>0.13</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="reading_lounge_proxy5">
          <pose>4.308332802840736 3.2258288929855032 0.065 0 0 -0.35</pose>
          <geometry>
            <cylinder>
              <radius>0.027</radius>
              <length>0.13</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="reading_lounge_proxy6">
          <pose>4.891667197159263 2.3741711070144964 0.065 0 0 -0.35</pose>
          <geometry>
            <cylinder>
              <radius>0.027</radius>
              <length>0.13</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="reading_lounge_proxy7">
          <pose>5.097405881632534 2.937794734722924 0.065 0 0 -0.35</pose>
          <geometry>
            <cylinder>
              <radius>0.027</radius>
              <length>0.13</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="reading_side_table_proxy0">
          <pose>5.6 2.6 0.49 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.3</radius>
              <length>0.055</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="reading_side_table_proxy1">
          <pose>5.6 2.6 0.23 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.045</radius>
              <length>0.46</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="reading_plant_proxy0">
          <pose>6.7 1.55 0.18 0 0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.22</radius>
              <length>0.36</length>
            </cylinder>
          </geometry>
        </collision>
        <collision name="entry_bench_proxy0">
          <pose>-4.3 -5.6 0.42 0 0 0</pose>
          <geometry>
            <box>
              <size>1.4 0.45 0.14</size>
            </box>
          </geometry>
        </collision>
        <collision name="entry_bench_proxy1">
          <pose>-4.859999999999999 -5.6 0.19 0 0 0</pose>
          <geometry>
            <box>
              <size>0.045 0.37 0.38</size>
            </box>
          </geometry>
        </collision>
        <collision name="entry_bench_proxy2">
          <pose>-3.7399999999999998 -5.6 0.19 0 0 0</pose>
          <geometry>
            <box>
              <size>0.045 0.37 0.38</size>
            </box>
          </geometry>
        </collision>
        <visual name="furnished_room">
          <geometry>
            <mesh>
              <uri>/home/robot/vacuum_ws/src/vacuum_sim/worlds/furnished/living_room.dae</uri>
            </mesh>
          </geometry>
          <cast_shadows>false</cast_shadows>
        </visual>
      </link>
    </model>
  </world>
</sdf>


## src/vacuum_sim/worlds/furnished

## src/vacuum_sim/worlds/furnished/linen.png

## src/vacuum_sim/worlds/furnished/window_plant.dae

## src/vacuum_sim/worlds/furnished/oak_media_console.dae

## src/vacuum_sim/worlds/furnished/woven-rug.png

## src/vacuum_sim/worlds/furnished/dining_table.dae

## src/vacuum_sim/worlds/furnished/dining_chair_north.dae

## src/vacuum_sim/worlds/furnished/architecture.dae

## src/vacuum_sim/worlds/furnished/bookcase.dae

## src/vacuum_sim/worlds/furnished/landscape.png

## src/vacuum_sim/worlds/furnished/dining_chair_west.dae

## src/vacuum_sim/worlds/furnished/rounded_coffee_table.dae

## src/vacuum_sim/worlds/furnished/framed_wall_art.dae

## src/vacuum_sim/worlds/furnished/garden.png

## src/vacuum_sim/worlds/furnished/three_seat_sofa.dae

## src/vacuum_sim/worlds/furnished/entry_plant.dae

## src/vacuum_sim/worlds/furnished/oak.png

## src/vacuum_sim/worlds/furnished/floor_lamp.dae

## src/vacuum_sim/worlds/furnished/office_chair.dae

## src/vacuum_sim/worlds/furnished/woven_living_room_rug.dae

## src/vacuum_sim/worlds/furnished/living_room.dae

## src/vacuum_sim/worlds/furnished/dining_chair_south.dae

## src/vacuum_sim/worlds/furnished/home_office_desk.dae

## src/vacuum_sim/urdf

## src/vacuum_sim/urdf/vacuum.urdf.xacro

<robot xmlns:xacro="http://www.ros.org/wiki/xacro" name="vacuum">
  <xacro:arg name="controllers_file" default="$(find vacuum_sim)/config/controllers.yaml" />
  <xacro:arg name="camera_width" default="320" />
  <xacro:arg name="camera_height" default="240" />
  <xacro:arg name="camera_rate" default="60" />
  <xacro:property name="wheel_radius" value="0.035" />
  <xacro:property name="wheel_separation" value="0.22" />
  <xacro:property name="wheel_width" value="0.025" />
  <xacro:property name="body_x" value="0.30" />
  <xacro:property name="body_y" value="0.25" />
  <xacro:property name="body_z" value="0.08" />
  <xacro:property name="body_mass" value="3.0" />
  <material name="acrylic">
    <color rgba=".17 .70 .77 .55" />
  </material>
  <material name="rubber">
    <color rgba=".055 .065 .075 1" />
  </material>
  <material name="sensor">
    <color rgba=".08 .10 .14 1" />
  </material>
  <link name="base_footprint" />
  <joint name="base_joint" type="fixed">
    <parent link="base_footprint" />
    <child link="base_link" />
    <origin xyz="-0.03 0 0.116" />
  </joint>
  <link name="base_link">
    <inertial>
      <mass value="${body_mass}" />
      <inertia ixx="${body_mass*(3*0.15**2+body_z**2)/12}" iyy="${body_mass*(3*0.15**2+body_z**2)/12}" izz="${body_mass*0.15**2/2}" ixy="0" ixz="0" iyz="0" />
    </inertial>
    <collision>
      <geometry>
        <cylinder radius="0.15" length="${body_z}" />
      </geometry>
    </collision>
    <visual name="lower_acrylic_chassis">
      <origin xyz="0 0 -0.038" />
      <geometry>
        <cylinder radius="0.15" length="0.004" />
      </geometry>
      <material name="acrylic" />
    </visual>
    <visual name="upper_acrylic_chassis">
      <origin xyz="0 0 0.038" />
      <geometry>
        <cylinder radius="0.15" length="0.004" />
      </geometry>
      <material name="acrylic" />
    </visual>
    <visual name="standoff_-0.08_-0.075">
      <origin xyz="-0.08 -0.075 0" />
      <geometry>
        <cylinder radius="0.004" length="0.072" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="standoff_-0.08_0.075">
      <origin xyz="-0.08 0.075 0" />
      <geometry>
        <cylinder radius="0.004" length="0.072" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="standoff_0.08_-0.075">
      <origin xyz="0.08 -0.075 0" />
      <geometry>
        <cylinder radius="0.004" length="0.072" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="standoff_0.08_0.075">
      <origin xyz="0.08 0.075 0" />
      <geometry>
        <cylinder radius="0.004" length="0.072" />
      </geometry>
      <material name="aluminium" />
    </visual>
  </link>
  <xacro:macro name="wheel" params="side sign">
    <link name="${side}_wheel">
      <inertial>
        <mass value="0.12" />
        <inertia ixx="${0.12*(3*wheel_radius**2+wheel_width**2)/12}" iyy="${0.12*wheel_radius**2/2}" izz="${0.12*(3*wheel_radius**2+wheel_width**2)/12}" ixy="0" ixz="0" iyz="0" />
      </inertial>
      <visual>
        <origin rpy="${pi/2} 0 0" />
        <geometry>
          <cylinder radius="${wheel_radius}" length="${wheel_width}" />
        </geometry>
        <material name="rubber" />
      </visual>
      <collision>
        <origin rpy="${pi/2} 0 0" />
        <geometry>
          <cylinder radius="${wheel_radius}" length="${wheel_width}" />
        </geometry>
      </collision>
    </link>
    <joint name="${side}_wheel_joint" type="continuous">
      <parent link="base_link" />
      <child link="${side}_wheel" />
      <origin xyz="0.03 ${sign*wheel_separation/2} ${wheel_radius-0.116}" />
      <axis xyz="0 1 0" />
      <limit effort="3.0" velocity="70.0" />
      <dynamics damping="0.01" friction="0.0" />
    </joint>
    <gazebo reference="${side}_wheel">
      <mu1>1.0</mu1>
      <mu2>1.0</mu2>
    </gazebo>
  </xacro:macro>
  <xacro:wheel side="left" sign="1" />
  <xacro:wheel side="right" sign="-1" />
  <joint name="caster_joint" type="fixed">
    <parent link="base_link" />
    <child link="caster" />
    <origin xyz="-0.105 0 -0.096" />
  </joint>
  <link name="caster">
    <inertial>
      <mass value="0.08" />
      <inertia ixx="0.0000128" iyy="0.0000128" izz="0.0000128" ixy="0" ixz="0" iyz="0" />
    </inertial>
    <visual>
      <geometry>
        <sphere radius="0.02" />
      </geometry>
      <material name="rubber" />
    </visual>
    <collision>
      <geometry>
        <sphere radius="0.02" />
      </geometry>
    </collision>
  </link>
  <gazebo reference="caster_joint">
    <preserveFixedJoint>true</preserveFixedJoint>
  </gazebo>
  <gazebo reference="caster">
    <mu1>0.01</mu1>
    <mu2>0.01</mu2>
  </gazebo>
  <joint name="lidar_joint" type="fixed">
    <parent link="base_link" />
    <child link="lidar_link" />
    <origin xyz="0 0 0.085" />
  </joint>
  <link name="lidar_link">
    <inertial>
      <mass value="0.05" />
      <inertia ixx="0.00001" iyy="0.00001" izz="0.00002" ixy="0" ixz="0" iyz="0" />
    </inertial>
    <collision>
      <geometry>
        <cylinder radius="0.03" length="0.025" />
      </geometry>
    </collision>
    <visual name="rplidar_mount_standoff">
      <origin xyz="0 0 -0.03" />
      <geometry>
        <cylinder radius="0.01" length="0.032" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="rplidar_c1_base">
      <origin xyz="0 0 -0.009" />
      <geometry>
        <box size="0.054 0.054 0.012" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="rplidar_c1_scanner">
      <origin xyz="0 0 0.005" />
      <geometry>
        <cylinder radius="0.027" length="0.025" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="rplidar_c1_accent">
      <origin xyz="0 0 0.015" />
      <geometry>
        <cylinder radius="0.025" length="0.004" />
      </geometry>
      <material name="copper" />
    </visual>
  </link>
  <gazebo reference="lidar_joint">
    <preserveFixedJoint>true</preserveFixedJoint>
  </gazebo>
  <gazebo reference="lidar_link">
    <sensor name="lidar" type="gpu_lidar">
      <topic>/scan</topic>
      <gz_frame_id>lidar_link</gz_frame_id>
      <update_rate>10.0</update_rate>
      <always_on>true</always_on>
      <lidar>
        <scan>
          <horizontal>
            <samples>500</samples>
            <resolution>1</resolution>
            <min_angle>${-pi}</min_angle>
            <max_angle>${pi}</max_angle>
          </horizontal>
        </scan>
        <range>
          <min>0.05</min>
          <max>12.0</max>
          <resolution>0.01</resolution>
        </range>
        <noise>
          <type>gaussian</type>
          <mean>0</mean>
          <stddev>0.015</stddev>
        </noise>
      </lidar>
    </sensor>
  </gazebo>
  <joint name="camera_joint" type="fixed">
    <parent link="base_link" />
    <child link="camera_link" />
    <origin xyz="0.1325 0 0.025" />
  </joint>
  <link name="camera_link">
    <inertial>
      <mass value="0.03" />
      <inertia ixx="0.000004" iyy="0.000004" izz="0.000004" ixy="0" ixz="0" iyz="0" />
    </inertial>
    <visual>
      <geometry>
        <box size="0.015 0.04 0.025" />
      </geometry>
      <material name="sensor" />
    </visual>
  </link>
  <joint name="camera_optical_joint" type="fixed">
    <parent link="camera_link" />
    <child link="camera_optical_frame" />
    <origin rpy="${-pi/2} 0 ${-pi/2}" />
  </joint>
  <link name="camera_optical_frame" />
  <gazebo reference="camera_joint">
    <preserveFixedJoint>true</preserveFixedJoint>
  </gazebo>
  <gazebo reference="camera_link">
    <sensor name="camera" type="camera">
      <topic>/camera/image_raw</topic>
      <gz_frame_id>camera_optical_frame</gz_frame_id>
      <update_rate>$(arg camera_rate)</update_rate>
      <always_on>true</always_on>
      <camera>
        <horizontal_fov>1.0472</horizontal_fov>
        <image>
          <width>$(arg camera_width)</width>
          <height>$(arg camera_height)</height>
          <format>R8G8B8</format>
        </image>
        <clip>
          <near>0.03</near>
          <far>15</far>
        </clip>
        <camera_info_topic>/camera/camera_info</camera_info_topic>
      </camera>
    </sensor>
  </gazebo>
  <ros2_control name="VacuumSimulation" type="system">
    <hardware>
      <plugin>gz_ros2_control/GazeboSimSystem</plugin>
    </hardware>
    <joint name="left_wheel_joint">
      <command_interface name="velocity" />
      <state_interface name="position" />
      <state_interface name="velocity" />
    </joint>
    <joint name="right_wheel_joint">
      <command_interface name="velocity" />
      <state_interface name="position" />
      <state_interface name="velocity" />
    </joint>
  </ros2_control>
  <gazebo>
    <plugin filename="libgz_ros2_control-system.so" name="gz_ros2_control::GazeboSimROS2ControlPlugin">
      <parameters>$(arg controllers_file)</parameters>
      <ros>
        <remapping>/diff_drive_controller/odom:=/odom</remapping>
      </ros>
    </plugin>
  </gazebo>
  <material name="aluminium">
    <color rgba=".62 .68 .75 1" />
  </material>
  <material name="pcb">
    <color rgba=".06 .42 .25 1" />
  </material>
  <material name="pcb_blue">
    <color rgba=".06 .25 .52 1" />
  </material>
  <material name="copper">
    <color rgba=".95 .58 .18 1" />
  </material>
  <material name="terminal">
    <color rgba=".15 .61 .29 1" />
  </material>
  <joint name="left_nema17_mount" type="fixed">
    <parent link="base_link" />
    <child link="left_nema17" />
    <origin xyz="0.03 0.071 -0.081" />
  </joint>
  <link name="left_nema17">
    <inertial>
      <mass value="0.25" />
      <inertia ixx="7.061020833333332e-05" iyy="7.455374999999999e-05" izz="7.061020833333332e-05" ixy="0" ixz="0" iyz="0" />
    </inertial>
    <visual name="left_nema17_body">
      <origin xyz="0 0 0" />
      <geometry>
        <box size="0.0423 0.04 0.0423" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="endplate_-0.016">
      <origin xyz="0 -0.016 0" />
      <geometry>
        <box size="0.0423 0.008 0.0423" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="endplate_0.016">
      <origin xyz="0 0.016 0" />
      <geometry>
        <box size="0.0423 0.008 0.0423" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="shaft_and_hub">
      <origin xyz="0 0.031 0" rpy="${pi/2} 0 0" />
      <geometry>
        <cylinder radius="0.004" length="0.023" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="under_chassis_mount">
      <origin xyz="0 0 0.03" />
      <geometry>
        <box size="0.043 0.042 0.018" />
      </geometry>
      <material name="aluminium" />
    </visual>
  </link>
  <joint name="left_tb6600_mount" type="fixed">
    <parent link="base_link" />
    <child link="left_tb6600" />
    <origin xyz="0.078 0.044 -0.021" />
  </joint>
  <link name="left_tb6600">
    <inertial>
      <mass value="0.1" />
      <inertia ixx="1.7666666666666668e-05" iyy="5.504166666666667e-05" izz="6.144166666666668e-05" ixy="0" ixz="0" iyz="0" />
    </inertial>
    <visual name="left_tb6600_body">
      <origin xyz="0 0 0" />
      <geometry>
        <box size="0.077 0.038 0.026" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="cooling_fin_-0.025">
      <origin xyz="-0.025 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="cooling_fin_-0.015">
      <origin xyz="-0.015 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="cooling_fin_-0.005">
      <origin xyz="-0.005 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="cooling_fin_0.005">
      <origin xyz="0.005 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="cooling_fin_0.015">
      <origin xyz="0.015 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="cooling_fin_0.025">
      <origin xyz="0.025 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="screw_terminals">
      <origin xyz="0 -0.022 0" />
      <geometry>
        <box size="0.065 0.01 0.018" />
      </geometry>
      <material name="terminal" />
    </visual>
  </link>
  <joint name="right_nema17_mount" type="fixed">
    <parent link="base_link" />
    <child link="right_nema17" />
    <origin xyz="0.03 -0.071 -0.081" />
  </joint>
  <link name="right_nema17">
    <inertial>
      <mass value="0.25" />
      <inertia ixx="7.061020833333332e-05" iyy="7.455374999999999e-05" izz="7.061020833333332e-05" ixy="0" ixz="0" iyz="0" />
    </inertial>
    <visual name="right_nema17_body">
      <origin xyz="0 0 0" />
      <geometry>
        <box size="0.0423 0.04 0.0423" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="endplate_-0.016">
      <origin xyz="0 -0.016 0" />
      <geometry>
        <box size="0.0423 0.008 0.0423" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="endplate_0.016">
      <origin xyz="0 0.016 0" />
      <geometry>
        <box size="0.0423 0.008 0.0423" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="shaft_and_hub">
      <origin xyz="0 -0.031 0" rpy="${pi/2} 0 0" />
      <geometry>
        <cylinder radius="0.004" length="0.023" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="under_chassis_mount">
      <origin xyz="0 0 0.03" />
      <geometry>
        <box size="0.043 0.042 0.018" />
      </geometry>
      <material name="aluminium" />
    </visual>
  </link>
  <joint name="right_tb6600_mount" type="fixed">
    <parent link="base_link" />
    <child link="right_tb6600" />
    <origin xyz="0.078 -0.044 -0.021" />
  </joint>
  <link name="right_tb6600">
    <inertial>
      <mass value="0.1" />
      <inertia ixx="1.7666666666666668e-05" iyy="5.504166666666667e-05" izz="6.144166666666668e-05" ixy="0" ixz="0" iyz="0" />
    </inertial>
    <visual name="right_tb6600_body">
      <origin xyz="0 0 0" />
      <geometry>
        <box size="0.077 0.038 0.026" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="cooling_fin_-0.025">
      <origin xyz="-0.025 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="cooling_fin_-0.015">
      <origin xyz="-0.015 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="cooling_fin_-0.005">
      <origin xyz="-0.005 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="cooling_fin_0.005">
      <origin xyz="0.005 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="cooling_fin_0.015">
      <origin xyz="0.015 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="cooling_fin_0.025">
      <origin xyz="0.025 0 0.016" />
      <geometry>
        <box size="0.003 0.038 0.009" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="screw_terminals">
      <origin xyz="0 0.022 0" />
      <geometry>
        <box size="0.065 0.01 0.018" />
      </geometry>
      <material name="terminal" />
    </visual>
  </link>
  <joint name="arduino_mega_mount" type="fixed">
    <parent link="base_link" />
    <child link="arduino_mega" />
    <origin xyz="-0.044 0.056 -0.027" />
  </joint>
  <link name="arduino_mega">
    <inertial>
      <mass value="0.037" />
      <inertia ixx="8.787160833333333e-06" iyy="3.1805540399999995e-05" izz="4.053720123333333e-05" ixy="0" ixz="0" iyz="0" />
    </inertial>
    <visual name="arduino_mega_body">
      <origin xyz="0 0 0" />
      <geometry>
        <box size="0.10152 0.0533 0.003" />
      </geometry>
      <material name="pcb_blue" />
    </visual>
    <visual name="mega_processor">
      <origin xyz="-0.009 0 0.004" />
      <geometry>
        <box size="0.014 0.014 0.005" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="mega_pin_headers_-0.023">
      <origin xyz="0 -0.023 0.005" />
      <geometry>
        <box size="0.079 0.004 0.007" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="mega_pin_headers_0.023">
      <origin xyz="0 0.023 0.005" />
      <geometry>
        <box size="0.079 0.004 0.007" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="mega_usb">
      <origin xyz="-0.046 0 0.007" />
      <geometry>
        <box size="0.015 0.013 0.012" />
      </geometry>
      <material name="aluminium" />
    </visual>
  </link>
  <joint name="orange_pi5_mount" type="fixed">
    <parent link="base_link" />
    <child link="orange_pi5" />
    <origin xyz="-0.044 -0.054 -0.027" />
  </joint>
  <link name="orange_pi5">
    <inertial>
      <mass value="0.046" />
      <inertia ixx="1.476983333333333e-05" iyy="3.836783333333334e-05" izz="5.3068666666666676e-05" ixy="0" ixz="0" iyz="0" />
    </inertial>
    <visual name="orange_pi5_body">
      <origin xyz="0 0 0" />
      <geometry>
        <box size="0.1 0.062 0.003" />
      </geometry>
      <material name="pcb" />
    </visual>
    <visual name="rk3588s_heatsink">
      <origin xyz="0 0 0.009" />
      <geometry>
        <box size="0.025 0.025 0.016" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="heatsink_fin_-0.01">
      <origin xyz="-0.01 0 0.019" />
      <geometry>
        <box size="0.002 0.025 0.006" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="heatsink_fin_-0.005">
      <origin xyz="-0.005 0 0.019" />
      <geometry>
        <box size="0.002 0.025 0.006" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="heatsink_fin_0">
      <origin xyz="0 0 0.019" />
      <geometry>
        <box size="0.002 0.025 0.006" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="heatsink_fin_0.005">
      <origin xyz="0.005 0 0.019" />
      <geometry>
        <box size="0.002 0.025 0.006" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="heatsink_fin_0.01">
      <origin xyz="0.01 0 0.019" />
      <geometry>
        <box size="0.002 0.025 0.006" />
      </geometry>
      <material name="sensor" />
    </visual>
    <visual name="ethernet_port">
      <origin xyz="-0.04 0 0.007" />
      <geometry>
        <box size="0.019 0.016 0.014" />
      </geometry>
      <material name="aluminium" />
    </visual>
    <visual name="gpio_header">
      <origin xyz="0.009 0.026 0.006" />
      <geometry>
        <box size="0.05 0.005 0.009" />
      </geometry>
      <material name="sensor" />
    </visual>
  </link>
</robot>


## src/vacuum_sim/scripts

## src/vacuum_sim/scripts/twist_adapter.py

#!/usr/bin/env python3
"""Simulation-only adapter for Jazzy's unstamped teleop/Nav2 Twist messages.

Publishes only on receipt. The diff-drive controller enforces its 0.25 s timeout.
This module does not implement an emergency stop for a physical robot.
"""
import math
import rclpy
from geometry_msgs.msg import Twist, TwistStamped
from rclpy.node import Node


class TwistAdapter(Node):
    def __init__(self):
        super().__init__('simulation_twist_adapter')
        self.publisher = self.create_publisher(TwistStamped, '/diff_drive_controller/cmd_vel', 1)
        self.subscription = self.create_subscription(Twist, '/cmd_vel', self.on_twist, 1)

    def on_twist(self, message):
        outgoing = TwistStamped()
        outgoing.header.stamp = self.get_clock().now().to_msg()
        outgoing.header.frame_id = 'base_footprint'
        if math.isfinite(message.linear.x) and math.isfinite(message.angular.z):
            outgoing.twist.linear.x = max(-0.9, min(1.5, message.linear.x))
            outgoing.twist.angular.z = max(-2.4, min(2.4, message.angular.z))
        self.publisher.publish(outgoing)


def main():
    rclpy.init()
    node = TwistAdapter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()


## src/vacuum_sim/CMakeLists.txt

cmake_minimum_required(VERSION 3.8)
project(vacuum_sim)
find_package(ament_cmake REQUIRED)
install(DIRECTORY urdf config launch worlds DESTINATION share/${PROJECT_NAME})
install(PROGRAMS scripts/twist_adapter.py DESTINATION lib/${PROJECT_NAME})
ament_package()


## tools

## tools/activate_guard.py

"""Activate the standalone simulator collision guard for direct driving."""
import os
import time
import rclpy
from rclpy.node import Node
from lifecycle_msgs.srv import GetState, ChangeState


def main():
    rclpy.init()
    node = Node(f'vacuum_guard_start_{os.getpid()}')
    get = node.create_client(GetState, '/collision_monitor/get_state')
    change = node.create_client(ChangeState, '/collision_monitor/change_state')

    def result(future):
        deadline = time.monotonic() + 15
        while not future.done() and time.monotonic() < deadline:
            rclpy.spin_once(node, timeout_sec=.05)
        if not future.done():
            raise RuntimeError('Collision guard lifecycle request timed out.')
        return future.result()

    try:
        if not get.wait_for_service(timeout_sec=20) or not change.wait_for_service(timeout_sec=20):
            raise RuntimeError('Collision guard is not available.')
        state = result(get.call_async(GetState.Request())).current_state.id
        for expected, transition in ((1, 1), (2, 3)):
            if state == expected:
                request = ChangeState.Request()
                request.transition.id = transition
                if not result(change.call_async(request)).success:
                    raise RuntimeError('Collision guard could not be activated.')
                state = result(get.call_async(GetState.Request())).current_state.id
        if state != 3:
            raise RuntimeError(f'Collision guard is in state {state}, not active.')
        print('Collision guard active.', flush=True)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()


## tools/apply_robot_profile.py

"""Apply the user's simulator geometry and response profile with rollback."""
from datetime import datetime
import hashlib
import json
import re
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET
import yaml

WS = Path('/home/robot/vacuum_ws')
PACKAGE = WS / 'src/vacuum_sim'
XACRO = 'http://www.ros.org/wiki/xacro'
ET.register_namespace('xacro', XACRO)


def apply_profile():
    source = WS / 'tools/robot-profile.json'
    profile = json.loads(source.read_text())
    fingerprint = hashlib.sha256(source.read_bytes()+Path(__file__).read_bytes()).hexdigest()
    marker = WS / '.lab/hardware-profile-v2'
    if marker.exists() and marker.read_text().splitlines()[0] == fingerprint:
        return
    hardware, drive = profile['hardware'], profile['drive']
    radius = hardware['wheel_diameter_m'] / 2
    model = PACKAGE / 'urdf/vacuum.urdf.xacro'
    root = ET.fromstring(model.read_text())
    properties = {item.get('name'): item for item in root.findall(f'{{{XACRO}}}property')}
    for name, value in {'wheel_radius': radius, 'wheel_separation': hardware['wheel_separation_m'],
                        'body_z': .08, 'body_mass': 3.0}.items():
        properties[name].set('value', str(value))
    root.find("joint[@name='base_joint']/origin").set('xyz', '-0.03 0 0.116')
    wheel_macro = root.find(f'{{{XACRO}}}macro[@name="wheel"]')
    wheel_macro.find('joint/origin').set('xyz', '0.03 ${sign*wheel_separation/2} ${wheel_radius-0.116}')
    wheel_macro.find('joint/limit').set('velocity', '70.0')
    root.find("joint[@name='caster_joint']/origin").set('xyz', '-0.105 0 -0.096')
    body = root.find("link[@name='base_link']")
    for visual in list(body.findall('visual')):
        body.remove(visual)
    for name, rgba in {'acrylic': '.17 .70 .77 .55', 'rubber': '.055 .065 .075 1',
                       'sensor': '.08 .10 .14 1', 'aluminium': '.62 .68 .75 1',
                       'pcb': '.06 .42 .25 1', 'pcb_blue': '.06 .25 .52 1',
                       'copper': '.95 .58 .18 1', 'terminal': '.15 .61 .29 1'}.items():
        material = root.find(f"material[@name='{name}']")
        if material is None:
            material = ET.SubElement(root, 'material', name=name)
            ET.SubElement(material, 'color')
        material.find('color').set('rgba', rgba)

    def visual(link, name, position, shape, dimensions, material, rpy=None):
        item = ET.SubElement(link, 'visual', name=name)
        origin = ET.SubElement(item, 'origin', xyz=' '.join(map(str, position)))
        if rpy:
            origin.set('rpy', rpy)
        geometry = ET.SubElement(item, 'geometry')
        if shape == 'box':
            ET.SubElement(geometry, 'box', size=' '.join(map(str, dimensions)))
        else:
            ET.SubElement(geometry, 'cylinder', radius=str(dimensions[0]), length=str(dimensions[1]))
        ET.SubElement(item, 'material', name=material)

    for name, height in [('lower_acrylic_chassis', -.038), ('upper_acrylic_chassis', .038)]:
        visual(body, name, (0, 0, height), 'cylinder', (.15, .004), 'acrylic')
    for x in (-.08, .08):
        for y in (-.075, .075):
            visual(body, f'standoff_{x}_{y}', (x, y, 0), 'cylinder', (.004, .072), 'aluminium')

    # Fixed components remain explicit ROS links; main chassis envelope provides
    # collision volume for the electronics. Mass and module details are estimates.
    names = ('left_nema17', 'right_nema17', 'left_tb6600', 'right_tb6600', 'arduino_mega', 'orange_pi5')
    for child in list(root):
        if child.tag in ('joint', 'link') and child.get('name', '').replace('_mount', '') in names:
            root.remove(child)

    def component(name, position, dimensions, material, mass):
        joint = ET.SubElement(root, 'joint', name=name+'_mount', type='fixed')
        ET.SubElement(joint, 'parent', link='base_link'); ET.SubElement(joint, 'child', link=name)
        ET.SubElement(joint, 'origin', xyz=' '.join(map(str, position)))
        link = ET.SubElement(root, 'link', name=name)
        inertial = ET.SubElement(link, 'inertial'); ET.SubElement(inertial, 'mass', value=str(mass))
        x,y,z = dimensions
        ET.SubElement(inertial, 'inertia', ixx=str(mass*(y*y+z*z)/12),
                      iyy=str(mass*(x*x+z*z)/12), izz=str(mass*(x*x+y*y)/12), ixy='0', ixz='0', iyz='0')
        visual(link, name+'_body', (0,0,0), 'box', dimensions, material)
        return link

    for side, sign in [('left', 1), ('right', -1)]:
        motor = component(side+'_nema17', (.03, sign*.071, -.081), (.0423,.040,.0423), 'sensor', .25)
        for y in (-.016,.016):
            visual(motor, 'endplate_'+str(y), (0,y,0), 'box', (.0423,.008,.0423), 'aluminium')
        visual(motor, 'shaft_and_hub', (0,sign*.031,0), 'cylinder', (.004,.023), 'aluminium', '${pi/2} 0 0')
        visual(motor, 'under_chassis_mount', (0,0,.030), 'box', (.043,.042,.018), 'aluminium')
        driver = component(side+'_tb6600', (.078,sign*.044,-.021), (.077,.038,.026), 'sensor', .10)
        for x in (-.025,-.015,-.005,.005,.015,.025):
            visual(driver,'cooling_fin_'+str(x),(x,0,.016),'box',(.003,.038,.009),'aluminium')
        visual(driver, 'screw_terminals', (0,-sign*.022,0), 'box', (.065,.010,.018), 'terminal')
    mega = component('arduino_mega', (-.044,.056,-.027), (.10152,.0533,.003), 'pcb_blue', .037)
    visual(mega,'mega_processor',(-.009,0,.004),'box',(.014,.014,.005),'sensor')
    for y in (-.023,.023): visual(mega,'mega_pin_headers_'+str(y),(0,y,.005),'box',(.079,.004,.007),'sensor')
    visual(mega,'mega_usb',(-.046,0,.007),'box',(.015,.013,.012),'aluminium')
    orange = component('orange_pi5',(-.044,-.054,-.027),(.100,.062,.003),'pcb',.046)
    visual(orange,'rk3588s_heatsink',(0,0,.009),'box',(.025,.025,.016),'aluminium')
    for x in (-.01,-.005,0,.005,.01): visual(orange,'heatsink_fin_'+str(x),(x,0,.019),'box',(.002,.025,.006),'sensor')
    visual(orange,'ethernet_port',(-.04,0,.007),'box',(.019,.016,.014),'aluminium')
    visual(orange,'gpio_header',(.009,.026,.006),'box',(.05,.005,.009),'sensor')
    lidar = root.find("link[@name='lidar_link']")
    for item in list(lidar.findall('visual')): lidar.remove(item)
    visual(lidar,'rplidar_mount_standoff',(0,0,-.030),'cylinder',(.010,.032),'aluminium')
    visual(lidar,'rplidar_c1_base',(0,0,-.009),'box',(.054,.054,.012),'sensor')
    visual(lidar,'rplidar_c1_scanner',(0,0,.005),'cylinder',(.027,.025),'sensor')
    visual(lidar,'rplidar_c1_accent',(0,0,.015),'cylinder',(.025,.004),'copper')
    sensor = root.find("gazebo[@reference='lidar_link']/sensor")
    sensor.find('update_rate').text=str(profile['lidar']['scan_hz'])
    sensor.find('lidar/scan/horizontal/samples').text=str(profile['lidar']['samples'])
    sensor.find('lidar/range/min').text=str(profile['lidar']['min_range_m'])
    sensor.find('lidar/range/max').text=str(profile['lidar']['max_range_m'])
    sensor.find('lidar/noise/stddev').text='0.015'
    ET.indent(root, space='  ')
    updates = {model: ET.tostring(root, encoding='unicode')+'\n',
               PACKAGE/'config/robot-profile.json': json.dumps(profile,indent=2)+'\n'}
    controller = PACKAGE/'config/controllers.yaml'
    data=yaml.safe_load(controller.read_text()); p=data['diff_drive_controller']['ros__parameters']
    p.update(wheel_radius=radius, wheel_separation=hardware['wheel_separation_m'],
             publish_rate=60.0, cmd_vel_timeout=.25, velocity_rolling_window_size=drive['odometry_window_samples'])
    data['controller_manager']['ros__parameters']['update_rate']=60
    p.update({'linear.x.max_velocity':drive['forward_m_s'], 'linear.x.min_velocity':-drive['reverse_m_s'],
              'linear.x.max_acceleration':drive['acceleration_m_s2'], 'linear.x.min_acceleration':-drive['acceleration_m_s2'],
              'linear.x.has_jerk_limits':False, 'angular.z.max_velocity':drive['turn_rad_s'],
              'angular.z.min_velocity':-drive['turn_rad_s'], 'angular.z.max_acceleration':drive['angular_acceleration_rad_s2'],
              'angular.z.min_acceleration':-drive['angular_acceleration_rad_s2'], 'angular.z.has_jerk_limits':False})
    updates[controller]=yaml.safe_dump(data,sort_keys=False)
    adapter=PACKAGE/'scripts/twist_adapter.py'
    adapter_text=adapter.read_text().replace('enforces its 0.5 s timeout','enforces its 0.25 s timeout')
    adapter_text=re.sub(r'outgoing.twist.linear.x = .+',
                        f"outgoing.twist.linear.x = max(-{drive['reverse_m_s']}, min({drive['forward_m_s']}, message.linear.x))",adapter_text)
    adapter_text=re.sub(r'outgoing.twist.angular.z = .+',
                        f"outgoing.twist.angular.z = max(-{drive['turn_rad_s']}, min({drive['turn_rad_s']}, message.angular.z))",adapter_text)
    adapter_text=adapter_text.replace("'/diff_drive_controller/cmd_vel', 10", "'/diff_drive_controller/cmd_vel', 1")
    adapter_text=adapter_text.replace("'/cmd_vel', self.on_twist, 10", "'/cmd_vel', self.on_twist, 1")
    updates[adapter]=adapter_text
    for name in ('nav2.yaml','vacuum_nav2.yaml'):
        path=PACKAGE/'config'/name; data=yaml.safe_load(path.read_text()); guard=data['collision_monitor']['ros__parameters']
        for zone,front,rear,width in [('StopZone',.62,-.60,.20),('SlowZone',1.7,-1.2,.25)]:
            if zone not in guard:
                continue
            p=guard[zone]
            p['forward']['points']=str([[-.03,width],[-.03,-width],[front,-width],[front,width]])
            p['reverse']['points']=str([[rear,width],[rear,-width],[-.03,-width],[-.03,width]])
            for polygon in p['velocity_polygons']:
                item=p[polygon]
                item['linear_max']=2.0 if polygon!='reverse' else -.001
                item['linear_min']=-2.0 if polygon!='forward' else .001
                item['theta_min']=-3.;item['theta_max']=3.
        if 'FootprintApproach' in guard:
            guard['FootprintApproach']['time_before_collision']=.55
            guard['FootprintApproach']['simulation_time_step']=.02
        updates[path]=yaml.safe_dump(data,sort_keys=False)
    backup=WS/'model-backups'/datetime.now().strftime('hardware-v2-%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True)
    originals={path:path.read_bytes() if path.exists() else None for path in updates}
    for path,content in originals.items():
        if content is not None:
            saved=backup/path.relative_to(PACKAGE);saved.parent.mkdir(parents=True,exist_ok=True);saved.write_bytes(content)
    try:
        for path,value in updates.items(): path.write_text(value)
        result=subprocess.run(['/bin/bash','-lc','source env.sh; colcon build --symlink-install --packages-select vacuum_sim'],cwd=WS,text=True,capture_output=True,timeout=180)
        if result.returncode: raise RuntimeError(result.stdout+result.stderr)
        marker.write_text(fingerprint+'\n'+str(backup)+'\n')
    except BaseException:
        for path,value in originals.items():
            if value is None:path.unlink(missing_ok=True)
            else:path.write_bytes(value)
        raise
    print('Hardware profile applied: 70 mm wheels, under-chassis NEMA 17s, 1.5 m/s simulator drive.',flush=True)


if __name__ == '__main__': apply_profile()


## tools/prepare_lab.py

"""Apply the 30 cm chassis to the existing Ubuntu simulator, with rollback."""

from datetime import datetime

import math

from pathlib import Path

import subprocess

import xml.etree.ElementTree as ET

import yaml



WS = Path('/home/robot/vacuum_ws')

PACKAGE = WS / 'src/vacuum_sim'

XACRO = 'http://www.ros.org/wiki/xacro'

ET.register_namespace('xacro', XACRO)





def circle(radius, count=32):

    # Circumscribed polygon: never underestimate the circular shell.

    outer = radius / math.cos(math.pi / count)

    return [[round(-.03 + outer * math.cos(2 * math.pi * i / count), 6),

             round(outer * math.sin(2 * math.pi * i / count), 6)] for i in range(count)]





def prepare_driving_views():

    launch = PACKAGE / 'launch/sim.launch.py'

    text = launch.read_text()

    text = text.replace("DeclareLaunchArgument('camera_rate', default_value='5')",

                        "DeclareLaunchArgument('camera_rate', default_value='60')")

    if "DeclareLaunchArgument('rviz_config'" not in text:

        text = text.replace("DeclareLaunchArgument('rviz', default_value='true'),",

                            "DeclareLaunchArgument('rviz', default_value='true'),\n"

                            "        DeclareLaunchArgument('rviz_config', default_value=str(package / 'config/view.rviz')),")

        text = text.replace("arguments=['-d', str(package / 'config/view.rviz')]",

                            "arguments=['-d', LaunchConfiguration('rviz_config')]")

    compile(text, str(launch), 'exec')

    model = PACKAGE / 'urdf/vacuum.urdf.xacro'

    root = ET.fromstring(model.read_text())

    rate = root.find(f'{{{XACRO}}}arg[@name="camera_rate"]')

    if rate is None:

        raise RuntimeError('The camera rate argument is missing.')

    rate.set('default', '60')

    view = PACKAGE / 'config/view.rviz'

    data = yaml.safe_load(view.read_text())

    data['Visualization Manager']['Global Options']['Frame Rate'] = 60

    drive_data = yaml.safe_load(yaml.safe_dump(data))

    drive_data['Visualization Manager']['Global Options']['Fixed Frame'] = 'odom'

    drive_data['Visualization Manager']['Displays'] = [item for item in drive_data['Visualization Manager']['Displays']

                                                       if item.get('Class') != 'rviz_default_plugins/Map']

    updates = {launch: text, model: ET.tostring(root, encoding='unicode') + '\n',

               view: yaml.safe_dump(data, sort_keys=False),

               PACKAGE / 'config/drive.rviz': yaml.safe_dump(drive_data, sort_keys=False)}

    world = PACKAGE / 'worlds/room.sdf'

    scene = ET.fromstring(world.read_text())

    # 180 Hz physics divides into 60 Hz camera/control, 30 Hz odometry, 10 Hz lidar.

    # At the 1.5 m/s limit a physics step covers about 8.3 mm.

    scene.find('world/physics/max_step_size').text = '0.005555555555555556'

    updates[world] = ET.tostring(scene, encoding='unicode') + '\n'

    changed = {path: value for path, value in updates.items() if not path.exists() or path.read_text() != value}

    if not changed:

        return

    backup = WS / 'model-backups' / datetime.now().strftime('camera60-%Y%m%d-%H%M%S-%f')

    backup.mkdir(parents=True)

    originals = {path: path.read_bytes() if path.exists() else None for path in changed}

    for path, content in originals.items():

        if content is not None:

            saved = backup / path.relative_to(PACKAGE)

            saved.parent.mkdir(parents=True, exist_ok=True)

            saved.write_bytes(content)

    try:

        for path, value in changed.items():

            path.write_text(value)

        built = subprocess.run(['/bin/bash', '-lc',

                                'source env.sh; colcon build --symlink-install --packages-select vacuum_sim'],

                               cwd=WS, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)

        if built.returncode:

            raise RuntimeError('Camera configuration build failed: ' + built.stdout[-4000:])

    except BaseException:

        for path, content in originals.items():

            if content is None:

                path.unlink(missing_ok=True)

            else:

                path.write_bytes(content)

        raise

    print('Camera target set to 60 FPS; direct driving view prepared.', flush=True)





def prepare():

    model = PACKAGE / 'urdf/vacuum.urdf.xacro'

    marker = WS / '.lab/circular-model-v1'

    prepare_driving_views()

    from apply_robot_profile import apply_profile

    apply_profile()

    if marker.exists():

        return

    root = ET.fromstring(model.read_text())

    props = {p.get('name'): p for p in root.findall(f'{{{XACRO}}}property')}

    for key in ('body_x', 'body_y', 'body_z', 'body_mass', 'wheel_separation'):

        if key not in props:

            raise RuntimeError(f'Unexpected robot model: missing {key}; no geometry changes applied.')

    props['wheel_separation'].set('value', '0.22')

    body = root.find("link[@name='base_link']")

    if body is None:

        raise RuntimeError('Expected chassis link was not found.')

    root.find("joint[@name='base_joint']/origin").set('xyz', '-0.03 0 0.08')

    inertia = body.find('inertial/inertia')

    inertia.set('ixx', '${body_mass*(3*0.15**2+body_z**2)/12}')

    inertia.set('iyy', '${body_mass*(3*0.15**2+body_z**2)/12}')

    inertia.set('izz', '${body_mass*0.15**2/2}')

    geom = body.find('collision/geometry')

    geom.clear()

    ET.SubElement(geom, 'cylinder', radius='0.15', length='${body_z}')

    plates = 0

    for visual in body.findall('visual'):

        geom = visual.find('geometry')

        box = geom.find('box')

        if box is not None and 'body_x' in box.get('size', ''):

            geom.clear()

            ET.SubElement(geom, 'cylinder', radius='0.15', length='0.004')

            plates += 1

        elif geom.find('cylinder') is not None:

            plate = geom.find('cylinder')

            if plate.get('radius') == '0.15' and plate.get('length') == '0.004':

                plates += 1

    if plates != 2:

        raise RuntimeError('Expected two acrylic plates; no geometry changes applied.')

    wheel = root.find(f'{{{XACRO}}}macro[@name="wheel"]/joint/origin')

    wheel.set('xyz', '0.03 ${sign*wheel_separation/2} ${wheel_radius-0.08}')

    root.find("joint[@name='caster_joint']/origin").set('xyz', '-0.105 0 -0.06')

    root.find("joint[@name='camera_joint']/origin").set('xyz', '0.1325 0 0.025')

    updates = {model: ET.tostring(root, encoding='unicode') + '\n'}

    controllers = PACKAGE / 'config/controllers.yaml'

    data = yaml.safe_load(controllers.read_text())

    data['diff_drive_controller']['ros__parameters']['wheel_separation'] = .22

    updates[controllers] = yaml.safe_dump(data, sort_keys=False)

    for name in ('nav2.yaml', 'vacuum_nav2.yaml'):

        path = PACKAGE / 'config' / name

        data = yaml.safe_load(path.read_text())

        for costmap in ('local_costmap', 'global_costmap'):

            params = data[costmap][costmap]['ros__parameters']

            params.pop('robot_radius', None)

            params['footprint'] = str(circle(.15))

            params['footprint_padding'] = .02

        params = data['collision_monitor']['ros__parameters']

        if name == 'vacuum_nav2.yaml':

            params['cmd_vel_in_topic'] = '/vacuum/selected_cmd_vel'

        for zone, radius in (('StopZone', .23), ('SlowZone', .35)):

            if zone in params:

                params[zone]['points'] = str(circle(radius))

        updates[path] = yaml.safe_dump(data, sort_keys=False)

    view = PACKAGE / 'config/view.rviz'

    data = yaml.safe_load(view.read_text())

    data['Visualization Manager']['Global Options']['Fixed Frame'] = 'map'

    updates[view] = yaml.safe_dump(data, sort_keys=False)

    backup = WS / 'model-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')

    backup.mkdir(parents=True)

    originals = {path: path.read_bytes() for path in updates}

    for path, content in originals.items():

        saved = backup / path.relative_to(PACKAGE)

        saved.parent.mkdir(parents=True, exist_ok=True)

        saved.write_bytes(content)

    try:

        for path, text in updates.items():

            path.write_text(text)

        built = subprocess.run(['/bin/bash', '-lc',

                                'source env.sh; colcon build --symlink-install --packages-select vacuum_sim'],

                               cwd=WS, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)

        if built.returncode:

            raise RuntimeError('Model build failed: ' + built.stdout[-5000:])

        marker.parent.mkdir(exist_ok=True)

        marker.write_text('30 cm circular body; axle offset 3 cm; wheel separation 22 cm.\n'

                          f'Previous source files: {backup}\n'

                          'Previous navigation validation used the old body; rerun for this geometry.\n')

    except BaseException:

        for path, content in originals.items():

            path.write_bytes(content)

        raise

    print(f'30 cm circular chassis prepared. Previous source saved in {backup}', flush=True)





if __name__ == '__main__':

    prepare()



## tools/__pycache__

## tools/__pycache__/controller_bridge.cpython-312.pyc

## tools/__pycache__/command_gate.cpython-312.pyc

## tools/__pycache__/prepare_lab.cpython-312.pyc

## tools/__pycache__/apply_robot_profile.cpython-312.pyc

## tools/validate_lab.py

"""Test an already-running launcher lab. Commands only the simulated robot."""
import json
import math
from pathlib import Path
import subprocess
import time
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from nav2_msgs.action import NavigateToPose

WS = Path('/home/robot/vacuum_ws')
report = {'date': '2026-10-07', 'scope': 'simulator only', 'tests': {}}
rclpy.init()
node = Node('vacuum_lab_validation', parameter_overrides=[rclpy.parameter.Parameter('use_sim_time', value=True)])
odom = []
commands = []
node.create_subscription(Odometry, '/odom', odom.append, qos_profile_sensor_data)
node.create_subscription(Twist, '/vacuum/selected_cmd_vel', commands.append, 10)
client = ActionClient(node, NavigateToPose, '/navigate_to_pose')
bridge = None


def wait(predicate, seconds):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        rclpy.spin_once(node, timeout_sec=.05)
        if predicate():
            return True
    return bool(predicate())


def run(action):
    result = subprocess.run(['python3', 'tools/lab_controller.py', action], cwd=WS,
                            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=100)
    print(result.stdout, flush=True)
    if result.returncode:
        raise RuntimeError(result.stdout)


try:
    assert wait(lambda: bool(odom) and bool(commands), 20), 'No odometry / command gate'
    assert client.wait_for_server(timeout_sec=10)
    goal = NavigateToPose.Goal()
    goal.pose.header.frame_id = 'map'
    goal.pose.header.stamp = node.get_clock().now().to_msg()
    goal.pose.pose.position.x = .6
    goal.pose.pose.orientation.w = 1.
    future = client.send_goal_async(goal)
    assert wait(future.done, 10)
    handle = future.result()
    assert handle.accepted, 'Navigation goal rejected'
    outcome = handle.get_result_async()
    if not wait(outcome.done, 100):
        cancellation = handle.cancel_goal_async()
        wait(cancellation.done, 5)
        raise RuntimeError('Navigation timed out; goal cancelled')
    result = outcome.result()
    assert result.status == 4 and result.result.error_code == 0, str(result)
    report['tests']['circular_robot_goal'] = {'status': result.status, 'error_code': result.result.error_code}
    print('Circular robot navigation goal passed.', flush=True)
    run('save-map')
    report['tests']['map_save'] = True
    run('manual')
    logfile = (WS / '.lab/bridge-validation.log').open('w')
    bridge = subprocess.Popen(['python3', 'tools/controller_bridge.py'], cwd=WS,
                              stdin=subprocess.PIPE, stdout=logfile, stderr=subprocess.STDOUT, text=True)

    def exercise(held, seconds):
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            assert bridge.poll() is None, 'Manual bridge exited'
            bridge.stdin.write(json.dumps({'v': .10, 'w': 0., 'held': held}) + '\n')
            bridge.stdin.flush()
            rclpy.spin_once(node, timeout_sec=.05)
            time.sleep(.02)

    # Allow DDS services and subscriptions to connect while sending zero input.
    exercise(False, 5)
    assert abs(odom[-1].twist.twist.linear.x) < .02, 'Robot moved while disarmed'
    start = odom[-1].pose.pose.position
    before = (start.x, start.y)
    exercise(True, 3)
    end = odom[-1].pose.pose.position
    movement = math.hypot(end.x-before[0], end.y-before[1])
    assert movement > .08, f'Manual drive did not move: {movement}'
    exercise(False, 2)
    assert abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02
    report['tests']['manual_hold_and_release'] = {'movement_m': movement, 'released_speed_m_s': odom[-1].twist.twist.linear.x}
    exercise(True, 1)
    # Keep the bridge alive, but stop supplying packets. Steady-time watchdog must stop.
    assert wait(lambda: abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02, 4)
    report['tests']['input_timeout_stop'] = True
    bridge.stdin.close()
    bridge.wait(timeout=5)
    assert bridge.returncode == 0
    report['tests']['bridge_eof_cleanup'] = True
    report['passed'] = True
except Exception as exc:
    report['passed'] = False
    report['error'] = str(exc)
    raise
finally:
    if bridge and bridge.poll() is None:
        try:
            bridge.stdin.close()
            bridge.wait(timeout=5)
        except Exception:
            bridge.terminate()
    target = WS / 'validation/lab-20261007'
    target.mkdir(parents=True, exist_ok=True)
    (target / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2), flush=True)
    node.destroy_node()
    rclpy.shutdown()


## tools/diagnose_manual.py

import json,subprocess,time,rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
rclpy.init(); node=Node('diagnose_manual'); latest={}
for topic in ['/vacuum/manual_cmd_vel','/vacuum/selected_cmd_vel','/cmd_vel']:
    node.create_subscription(Twist,topic,lambda m,t=topic: latest.update({t:m.linear.x}),10)
node.create_subscription(Odometry,'/odom',lambda m:latest.update({'odom':m.twist.twist.linear.x}),10)
p=subprocess.Popen(['python3','tools/controller_bridge.py'],stdin=subprocess.PIPE,text=True)
started=time.monotonic(); next_print=0
try:
    while time.monotonic()-started<9:
        elapsed=time.monotonic()-started
        p.stdin.write(json.dumps({'v':.1,'w':0.,'held':3<elapsed<7})+'\n');p.stdin.flush()
        rclpy.spin_once(node,timeout_sec=.05);time.sleep(.02)
        if elapsed>=next_print:
            print(round(elapsed,2),latest,flush=True);next_print=elapsed+1
finally:
    p.stdin.close();p.wait(timeout=5);node.destroy_node();rclpy.shutdown()


## tools/lab_controller.py

#!/usr/bin/env python3
"""User-owned, simulator-only launcher. No sudo, hardware, or global process killing."""
import argparse
import datetime
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import time
import yaml

WS = Path('/home/robot/vacuum_ws')
RUN = WS / '.lab'
STATE = RUN / 'processes.json'
SESSION = RUN / 'session.json'
CAMERA_RATE = 60


def say(message):
    print(message, flush=True)


def identity(pid):
    try:
        path = Path(f'/proc/{pid}')
        # comm may contain spaces, so split after its closing parenthesis.
        fields = (path / 'stat').read_text().rsplit(')', 1)[1].split()
        if fields[0] == 'Z' or path.stat().st_uid != os.getuid():
            return None
        return fields[19]  # /proc stat field 22: start time
    except (FileNotFoundError, ProcessLookupError, PermissionError):
        return None


def read_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save(state):
    tmp = STATE.with_suffix('.tmp')
    tmp.write_text(json.dumps(state))
    tmp.replace(STATE)


def alive(record):
    return identity(record['pid']) == record['start']


def member_alive(pid, stamp, group):
    try:
        return identity(int(pid)) == stamp and os.getpgid(int(pid)) == group and os.getsid(int(pid)) == group
    except ProcessLookupError:
        return False


def group_members(record):
    result = {}
    if not alive(record):
        return {pid: stamp for pid, stamp in record.get('members', {}).items()
                if member_alive(pid, stamp, record['pid'])}
    for path in Path('/proc').iterdir():
        if not path.name.isdigit():
            continue
        try:
            fields = (path / 'stat').read_text().rsplit(')', 1)[1].split()
            if int(fields[2]) == record['pid'] and int(fields[3]) == record['pid']:
                stamp = identity(int(path.name))
                if stamp is not None:
                    result[path.name] = stamp
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            pass
    return result


def stop(state):
    # Reverse startup order. Never signal a recycled PID or another user's process.
    for name, record in reversed(list(state.items())):
        members = group_members(record)
        if not members:
            continue
        record['members'] = members
        save(state)
        def still_running():
            return any(member_alive(pid, stamp, record['pid'])
                       for pid, stamp in members.items())
        say(f'Stopping {name}…')
        for sig, delay in ((signal.SIGTERM, 14), (signal.SIGKILL, 2)):
            if not still_running():
                break
            try:
                os.killpg(record['pid'], sig)
            except ProcessLookupError:
                break
            end = time.monotonic() + delay
            while still_running() and time.monotonic() < end:
                time.sleep(.2)
    remaining = {name: rec for name, rec in state.items() if group_members(rec)}
    save(remaining)
    (RUN / 'manual-mode').unlink(missing_ok=True)
    SESSION.unlink(missing_ok=True)
    if remaining:
        raise RuntimeError('Some lab processes did not stop. See .lab logs.')


def command(argv, timeout=20):
    return subprocess.run(['/bin/bash', '-lc', 'source env.sh; exec "$@"',
                           'vacuum-lab', *argv], cwd=WS, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=timeout)


def launch(state, name, argv):
    with (RUN / f'{name}.log').open('w') as log:
        proc = subprocess.Popen(['/bin/bash', '-lc', 'source env.sh; exec "$@"',
                                 'vacuum-lab', *argv], cwd=WS, stdin=subprocess.DEVNULL,
                                stdout=log, stderr=subprocess.STDOUT,
                                start_new_session=True)
    state[name] = {'pid': proc.pid, 'start': identity(proc.pid)}
    if state[name]['start'] is None:
        raise RuntimeError(f'{name} exited during startup. See .lab/{name}.log.')
    save(state)


def ready(state, target, seconds=60):
    result = command(['python3', 'tools/wait_ready.py', target, '--timeout', str(seconds)], seconds + 10)
    if any(not alive(rec) for rec in state.values()):
        raise RuntimeError('A lab component exited. See .lab logs.')
    if result.returncode or 'READY' not in result.stdout:
        raise RuntimeError(f'{target} startup timed out. See .lab logs. ' + result.stdout)


def start(state, gazebo):
    settings = json.loads(SESSION.read_text()) if SESSION.exists() else {}
    if set(state) == {'simulation', 'command gate', 'mapping', 'navigation'} and all(alive(rec) for rec in state.values()) and settings.get('camera_rate') == CAMERA_RATE and not (RUN / 'manual-mode').exists():
        say('Lab is already running. Stop and restart to leave manual mode or change the views.')
        return
    if state:
        stop(state)
        state.clear()
    required = [WS / 'env.sh', WS / 'tools/run_sim.py',
                WS / 'src/vacuum_sim/config/vacuum_nav2.yaml',
                WS / 'src/vacuum_sim/config/vacuum_navigate.xml']
    if any(not path.is_file() for path in required):
        raise RuntimeError('The simulator or conservative navigation profile is missing.')
    # Refuse to combine this session with an existing manually started ROS workload.
    nodes = command(['ros2', 'node', 'list', '--no-daemon', '--spin-time', '2']).stdout
    if any(name in nodes for name in ('/slam_toolbox', '/controller_server', '/robot_state_publisher')):
        raise RuntimeError('A manual lab session is running. Stop its terminals first.')
    from prepare_lab import prepare
    checked = command(['python3', 'tools/check_lab.py'], 30)
    if checked.returncode:
        raise RuntimeError('Controller safety logic checks failed: ' + checked.stdout)
    prepare()
    try:
        say('Starting simulator and RViz…')
        launch(state, 'simulation', ['python3', 'tools/run_sim.py',
                                    f'gui:={str(gazebo).lower()}', 'rviz:=true',
                                    f'camera_rate:={CAMERA_RATE}',
                                    'rviz_config:=' + str(WS / 'src/vacuum_sim/config/view.rviz')])
        ready(state, 'scan')
        launch(state, 'command gate', ['python3', 'tools/command_gate.py'])
        say('Starting mapping…')
        launch(state, 'mapping', ['ros2', 'launch', 'vacuum_sim', 'mapping.launch.py'])
        ready(state, 'map')
        say('Starting obstacle-aware navigation…')
        launch(state, 'navigation', ['ros2', 'launch', 'vacuum_sim', 'navigation.launch.py',
                                    'params_file:=' + str(required[2])])
        ready(state, 'navigation')
        SESSION.write_text(json.dumps({'mode': 'navigation', 'camera_rate': CAMERA_RATE}))
        say('Ready. In RViz set Fixed Frame to map, then use Nav2 Goal to choose a destination.')
        say('This is mapping and destination navigation. Automatic room cleaning is not implemented.')
    except BaseException:
        say('Startup failed; stopping this launcher’s processes…')
        stop(state)
        raise


def drive(state, gazebo):
    settings = json.loads(SESSION.read_text()) if SESSION.exists() else {}
    if set(state) == {'simulation', 'command gate', 'collision guard', 'camera view'} and all(alive(rec) for rec in state.values()) and settings.get('camera_rate') == CAMERA_RATE:
        ready(state, 'collision_monitor', 15)
        say('Ready to drive. Open the controller panel; push forward, pull back to reverse.')
        return
    if state:
        stop(state)
        state.clear()
    nodes = command(['ros2', 'node', 'list', '--no-daemon', '--spin-time', '2']).stdout
    if any(name in nodes for name in ('/slam_toolbox', '/controller_server', '/robot_state_publisher', '/collision_monitor')):
        raise RuntimeError('A manual lab session is running. Stop its terminals first.')
    from prepare_lab import prepare, circle
    prepare()
    checked = command(['python3', 'tools/check_lab.py'], 30)
    if checked.returncode:
        raise RuntimeError('Controller safety checks failed: ' + checked.stdout)
    config = yaml.safe_load((WS / 'src/vacuum_sim/config/vacuum_nav2.yaml').read_text())
    guard = config['collision_monitor']['ros__parameters']
    # Static approach footprint preserves predictive braking without a costmap.
    guard['FootprintApproach']['points'] = str(circle(.17))
    guard['cmd_vel_in_topic'] = '/vacuum/selected_cmd_vel'
    guard_path = RUN / 'drive-guard.yaml'
    guard_path.write_text(yaml.safe_dump({'collision_monitor': {'ros__parameters': guard}}, sort_keys=False))
    (RUN / 'manual-mode').write_text('Direct manual driving selected.\n')
    try:
        say('Starting 60 FPS camera and driving view…')
        launch(state, 'simulation', ['python3', 'tools/run_sim.py',
                                    f'gui:={str(gazebo).lower()}', 'rviz:=false',
                                    f'camera_rate:={CAMERA_RATE}',
                                    'rviz_config:=' + str(WS / 'src/vacuum_sim/config/drive.rviz')])
        ready(state, 'scan')
        launch(state, 'command gate', ['python3', 'tools/command_gate.py'])
        launch(state, 'collision guard', ['/opt/ros/jazzy/lib/nav2_collision_monitor/collision_monitor',
                                         '--ros-args', '--params-file', str(guard_path)])
        activated = command(['python3', 'tools/activate_guard.py'], 65)
        if activated.returncode:
            raise RuntimeError(activated.stdout)
        launch(state, 'camera view', ['python3', '/opt/ros/jazzy/lib/rqt_image_view/rqt_image_view', '/camera/image_raw'])
        ready(state, 'collision_monitor', 15)
        SESSION.write_text(json.dumps({'mode': 'drive', 'camera_rate': CAMERA_RATE}))
        say('Ready to drive. Push forward, pull back to reverse. Camera target: 60 FPS.')
    except BaseException:
        say('Driving startup failed; stopping this launcher’s processes…')
        stop(state)
        raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['start', 'drive', 'stop', 'status', 'save-map', 'manual'])
    parser.add_argument('--gazebo', action='store_true')
    args = parser.parse_args()
    if not WS.is_dir():
        raise RuntimeError('Ubuntu vacuum workspace was not found.')
    RUN.mkdir(exist_ok=True)
    with (RUN / 'controller.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        state = read_state()
        if args.action == 'start':
            start(state, args.gazebo)
        elif args.action == 'drive':
            drive(state, args.gazebo)
        elif args.action == 'stop':
            stop(state)
            say('Lab stopped.')
        elif args.action == 'status':
            say('\n'.join(f'{name}: {"running" if alive(rec) else "stopped"}'
                          for name, rec in state.items()) or 'Lab is stopped.')
        elif args.action == 'manual':
            if set(state) == {'simulation', 'command gate', 'collision guard', 'camera view'} and all(alive(rec) for rec in state.values()):
                ready(state, 'collision_monitor', 15)
                say('Manual mode ready. Direct driving guard is active.')
                return
            if set(state) != {'simulation', 'command gate', 'mapping', 'navigation'} or any(not alive(rec) for rec in state.values()):
                raise RuntimeError('Start the lab before enabling manual drive.')
            # Switch the gate first: autonomous output cannot reach the robot,
            # even while cancellation is pending. Keep Nav2's managed nodes alive
            # so its bond manager does not tear down Collision Monitor.
            (RUN / 'manual-mode').write_text('Manual command source selected; restart to resume goals.\n')
            result = command(['ros2', 'service', 'call', '/navigate_to_pose/_action/cancel_goal',
                              'action_msgs/srv/CancelGoal', '{}'], 30)
            if result.returncode:
                raise RuntimeError('Could not cancel navigation; the gate remains stopped in manual mode. ' + result.stdout)
            ready(state, 'collision_monitor', 20)
            say('Manual mode ready. Navigation is paused until Stop lab → Start lab.')
        else:
            if not state.get('mapping') or not alive(state['mapping']):
                raise RuntimeError('Start the lab before saving a map.')
            maps = WS / 'maps'
            maps.mkdir(exist_ok=True)
            prefix = maps / datetime.datetime.now().strftime('room-%Y%m%d-%H%M%S-%f')
            result = command(['ros2', 'run', 'nav2_map_server', 'map_saver_cli',
                              '-f', str(prefix), '--ros-args', '-p', 'use_sim_time:=true',
                              '-p', 'save_map_timeout:=10.0',
                              '-p', 'map_subscribe_transient_local:=true'], 40)
            if result.returncode or not prefix.with_suffix('.yaml').is_file():
                raise RuntimeError('Map save failed: ' + result.stdout)
            say(f'Map saved: {prefix}.yaml\nSaved-map localization is a separate future workflow.')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        say(f'Error: {exc}')
        raise SystemExit(1)


## tools/controller_bridge.py

"""Manual simulator control via stdin; steady-time watchdog and Nav2 interlock."""

import json

import math

from pathlib import Path

import sys

import threading

import time

import rclpy

from geometry_msgs.msg import Twist

from lifecycle_msgs.srv import GetState

from nav2_msgs.msg import CollisionMonitorState

from nav_msgs.msg import Odometry

from sensor_msgs.msg import LaserScan

from rclpy.qos import qos_profile_sensor_data

from rclpy.node import Node



MODE = Path('/home/robot/vacuum_ws/.lab/manual-mode')

PROFILE = json.loads((Path(__file__).parent / 'robot-profile.json').read_text())['drive']





def decode(line):

    data = json.loads(line)

    v, w = float(data['v']), float(data['w'])

    if not math.isfinite(v) or not math.isfinite(w):

        raise ValueError('Non-finite control input')

    if data.get('enabled', data.get('held', False)) is not True:

        return 0., 0.

    return max(-PROFILE['reverse_m_s'], min(PROFILE['forward_m_s'], v)), max(-PROFILE['turn_rad_s'], min(PROFILE['turn_rad_s'], w))





class Bridge(Node):

    def __init__(self):

        super().__init__('vacuum_manual_controller')

        self.pub = self.create_publisher(Twist, '/vacuum/manual_cmd_vel', 1)

        self.lock = threading.Lock()

        self.latest = (0., 0.)

        self.received = 0.

        self.closed = False

        self.states = {'collision_monitor': (0, 0.)}

        self.state_clients = {name: self.create_client(GetState, f'/{name}/get_state') for name in self.states}

        self.pending = {}

        self.last_status = None

        self.report_at = 0.

        self.guard_action = (0, '')

        self.output = (0., 0., 0.)

        self.scan_at = 0.

        self.odom = (0., 0., 0.)

        self.motion_since = 0.

        self.create_subscription(CollisionMonitorState, '/collision_monitor_state', self.guard_state, 10)

        self.create_subscription(Twist, '/cmd_vel', self.guard_output, 1)

        self.create_subscription(LaserScan, '/scan', self.scan_received, qos_profile_sensor_data)

        self.create_subscription(Odometry, '/odom', self.odom_received, qos_profile_sensor_data)

        self.create_timer(PROFILE['input_period_s'], self.tick)

        self.create_timer(.25, self.check_states)

        threading.Thread(target=self.read_input, daemon=True).start()



    def read_input(self):

        try:

            for line in sys.stdin:

                try:

                    command = decode(line)

                except (ValueError, KeyError, TypeError):

                    command = (0., 0.)

                with self.lock:

                    self.latest = command

                    self.received = time.monotonic()

        finally:

            with self.lock:

                self.latest = (0., 0.)

                self.closed = True



    def check_states(self):

        now = time.monotonic()

        for name, client in self.state_clients.items():

            previous = self.pending.get(name)

            if previous and not previous[0].done():

                if now - previous[1] < .75:

                    continue

                # A lost service response must not leave a permanently pending

                # future that prevents all subsequent health checks.

                self.pending.pop(name)

                client.remove_pending_request(previous[0])

                previous[0].cancel()

            if not client.service_is_ready():

                continue

            future = client.call_async(GetState.Request())

            self.pending[name] = (future, now)

            future.add_done_callback(lambda result, name=name: self.record(name, result))



    def record(self, name, future):

        if self.pending.get(name, (None,))[0] is not future:

            return

        try:

            self.states[name] = (future.result().current_state.id, time.monotonic())

        except Exception:

            self.states[name] = (0, 0.)



    def guard_state(self, message):

        self.guard_action = (message.action_type, message.polygon_name)



    def guard_output(self, message):

        self.output = (message.linear.x, message.angular.z, time.monotonic())



    def scan_received(self, message):

        self.scan_at = time.monotonic()



    def odom_received(self, message):

        self.odom = (message.twist.twist.linear.x, message.twist.twist.angular.z, time.monotonic())



    def report(self, now, safe, v, w):

        if now < self.report_at:

            return

        self.report_at = now + .25

        out_v, out_w, stamp = self.output

        actual_v, actual_w, odom_stamp = self.odom

        action, polygon = self.guard_action

        reason = 'Ready'

        if not MODE.exists():

            reason = 'Manual mode is not selected'

        elif now - self.scan_at > .5:

            reason = 'Lidar data missing or stale; guard stops motion'

        elif not safe:

            reason = 'Waiting for collision guard health; commands stopped'

        elif abs(v) + abs(w) > .001:

            if now - stamp > .5:

                reason = 'No fresh guard output; commands stopped'

            elif abs(out_v) + abs(out_w) < .001:

                if action and polygon:

                    escape = 'try reverse' if v > .001 else ('try forward' if v < -.001 else 'move away before turning')

                    reason = 'Obstacle blocks this direction; ' + escape

                else:

                    reason = 'Guard stopped motion; check lidar/TF in Ubuntu logs'

            elif abs(out_v) < abs(v) - .01 or abs(out_w) < abs(w) - .01:

                reason = 'Slowing near an obstacle'

            else:

                reason = 'Driving'

                if now - odom_stamp > 1.:

                    reason = 'Odometry missing; check simulator/controller'

                elif self.motion_since and now - self.motion_since > 1.5 and abs(actual_v) < .015 and abs(actual_w) < .04:

                    reason = 'No actual movement; STOP and check simulator/controller'

        print(json.dumps({'ready': safe, 'reason': reason, 'polygon': polygon,

                          'requested_v': v, 'output_v': out_v, 'output_w': out_w,

                          'actual_v': actual_v, 'actual_w': actual_w}), flush=True)



    def tick(self):

        now = time.monotonic()

        safe = MODE.exists() and now - self.scan_at < .5 and all(state == 3 and now - stamp < 1.

                                     for state, stamp in self.states.values())

        with self.lock:

            v, w = self.latest if safe and now - self.received < .3 else (0., 0.)

            closed = self.closed

        message = Twist()

        message.linear.x, message.angular.z = v, w

        if abs(v) + abs(w) > .03:

            if not self.motion_since:

                self.motion_since = now

        else:

            self.motion_since = 0.

        self.pub.publish(message)

        self.report(now, safe, v, w)

        if closed:

            raise KeyboardInterrupt





def main():

    # The launcher lock, separate from the simulator lock, serializes manual sources.

    import fcntl

    path = Path('/home/robot/vacuum_ws/.lab/manual-input.lock')

    with path.open('a') as lock:

        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)

        rclpy.init()

        node = Bridge()

        try:

            rclpy.spin(node)

        except KeyboardInterrupt:

            pass

        finally:

            node.pub.publish(Twist())

            node.destroy_node()

            if rclpy.ok():

                rclpy.shutdown()





if __name__ == '__main__':

    main()



## tools/wait_ready.py

"""Wait for live ROS messages/services, without the ros2 CLI graph cache."""
import argparse
import os
import time
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy, qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid
from lifecycle_msgs.srv import GetState


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', choices=['scan', 'map', 'navigation', 'collision_monitor'])
    parser.add_argument('--timeout', type=float, default=60)
    args = parser.parse_args()
    rclpy.init()
    node = Node(f'vacuum_lab_readiness_{os.getpid()}')
    received = []
    clients = {}
    pending = {}
    active = set()
    if args.target == 'scan':
        node.create_subscription(LaserScan, '/scan', received.append, qos_profile_sensor_data)
    elif args.target == 'map':
        node.create_subscription(OccupancyGrid, '/map', received.append,
                                 QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL,
                                            reliability=ReliabilityPolicy.RELIABLE))
    else:
        names = ['controller_server', 'planner_server', 'collision_monitor', 'bt_navigator'] if args.target == 'navigation' else ['collision_monitor']
        clients = {name: node.create_client(GetState, f'/{name}/get_state') for name in names}
    deadline = time.monotonic() + args.timeout
    next_call = 0.
    try:
        while time.monotonic() < deadline:
            rclpy.spin_once(node, timeout_sec=.05)
            if received or (clients and len(active) == len(clients)):
                print('READY', flush=True)
                return 0
            if time.monotonic() >= next_call:
                for name, client in clients.items():
                    request = pending.get(name)
                    future = request[0] if request else None
                    if future and not future.done():
                        if time.monotonic() - request[1] < 2.:
                            continue
                        client.remove_pending_request(future)
                        future.cancel()
                        pending.pop(name)
                        active.discard(name)
                        future = None
                    if future:
                        try:
                            if future.result().current_state.id == 3:
                                active.add(name)
                            else:
                                active.discard(name)
                        except Exception:
                            active.discard(name)
                    if client.service_is_ready():
                        pending[name] = (client.call_async(GetState.Request()), time.monotonic())
                next_call = time.monotonic() + .5
        missing = sorted(set(clients)-active)
        print(f'Not ready: {args.target}' + (f'; waiting for {", ".join(missing)}' if missing else ''), flush=True)
        return 1
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    raise SystemExit(main())


## tools/validate_autonomy.py

#!/usr/bin/env python3
"""Simulator-only integration checks; isolated guard output cannot command motors."""
import copy
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import time
import yaml
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy, qos_profile_sensor_data
from geometry_msgs.msg import Twist
from lifecycle_msgs.srv import ChangeState, GetState
from nav_msgs.msg import OccupancyGrid, Odometry
from nav2_msgs.action import NavigateToPose
from sensor_msgs.msg import LaserScan

ws=Path('/home/robot/vacuum_ws')
logs=ws/'validation/autonomy-20261006'
logs.mkdir(parents=True,exist_ok=True)
processes=[]
handles=[]
def start(name,args):
    log=(logs/(name+'.log')).open('w')
    handles.append(log)
    p=subprocess.Popen(args,cwd=ws,stdout=log,stderr=subprocess.STDOUT,
                       stdin=subprocess.DEVNULL,start_new_session=True)
    processes.append(p)
    return p

def cleanup():
    for p in reversed(processes):
        try:
            os.killpg(p.pid,signal.SIGINT)
            p.wait(timeout=8)
        except (ProcessLookupError,subprocess.TimeoutExpired):
            pass
        try:
            os.killpg(p.pid,signal.SIGTERM)
            p.wait(timeout=2)
        except (ProcessLookupError,subprocess.TimeoutExpired):
            pass
    for log in handles:
        log.close()

rclpy.init()
node=Node('vacuum_autonomy_validation',parameter_overrides=[rclpy.parameter.Parameter('use_sim_time',value=True)])
maps=[]
odom=[]
subscriptions=[
    node.create_subscription(OccupancyGrid,'/map',maps.append,QoSProfile(depth=1,durability=DurabilityPolicy.TRANSIENT_LOCAL,reliability=ReliabilityPolicy.RELIABLE)),
    node.create_subscription(Odometry,'/odom',odom.append,qos_profile_sensor_data)]
client=ActionClient(node,NavigateToPose,'/navigate_to_pose')
result={'date':'2026-10-06','scope':'Ubuntu vacuum simulator only','tests':{}}
def wait(predicate,seconds):
    end=time.monotonic()+seconds
    while not predicate() and time.monotonic()<end:
        rclpy.spin_once(node,timeout_sec=0.05)
    return predicate()
def goal(x,y,timeout=90):
    request=NavigateToPose.Goal()
    request.pose.header.frame_id='map'
    request.pose.header.stamp=node.get_clock().now().to_msg()
    request.pose.pose.position.x=x
    request.pose.pose.position.y=y
    request.pose.pose.orientation.w=1.0
    future=client.send_goal_async(request)
    assert wait(future.done,10),'Goal submission timed out'
    handle=future.result()
    assert handle and handle.accepted,'Goal rejected'
    future=handle.get_result_async()
    if not wait(future.done,timeout):
        cancellation=handle.cancel_goal_async()
        wait(cancellation.done,5)
        raise RuntimeError('Goal timed out and was cancelled')
    return future.result()

try:
    start('sim',['python3','tools/run_sim.py','gui:=false','rviz:=false'])
    assert wait(lambda: bool(odom),40),'Simulator odometry unavailable'
    start('mapping',['ros2','launch','vacuum_sim','mapping.launch.py'])
    assert wait(lambda: bool(maps),30),'SLAM map unavailable'
    start('navigation',['ros2','launch','vacuum_sim','navigation.launch.py',
          'params_file:='+str(ws/'src/vacuum_sim/config/vacuum_nav2.yaml')])
    assert client.wait_for_server(timeout_sec=40),'Nav2 action endpoint unavailable'
    for name in ('bt_navigator','controller_server','planner_server','collision_monitor'):
        service=node.create_client(GetState,'/'+name+'/get_state')
        assert service.wait_for_service(timeout_sec=20),name+' lifecycle unavailable'
        deadline=time.monotonic()+40
        active=False
        while time.monotonic()<deadline:
            state=service.call_async(GetState.Request())
            if wait(state.done,3) and state.result().current_state.id==3:
                active=True
                break
            end=time.monotonic()+.3
            while time.monotonic()<end:
                rclpy.spin_once(node,timeout_sec=.05)
        assert active,name+' never activated'
    outcome=goal(1.0,0.0)
    assert outcome.status==4 and outcome.result.error_code==0, str(outcome)
    result['tests']['free_space_goal']={'status':outcome.status,'error_code':outcome.result.error_code}
    before=copy.deepcopy(odom[-1].pose.pose.position)
    outcome=goal(3.15,0.0,40)
    assert outcome.status==6,'Goal beyond room wall should abort'
    end=time.monotonic()+2
    while time.monotonic()<end:
        rclpy.spin_once(node,timeout_sec=.05)
    after=odom[-1].pose.pose.position
    movement=math.hypot(after.x-before.x,after.y-before.y)
    assert movement<.10 and abs(odom[-1].twist.twist.linear.x)<.02,'Robot moved toward blocked wall goal'
    result['tests']['goal_beyond_wall']={'status':outcome.status,'movement_m':movement}

    # An isolated copy of the exact configured collision guard. Its output has no
    # connection to the robot's /cmd_vel adapter; only synthetic scans are injected.
    p=copy.deepcopy(yaml.safe_load((ws/'src/vacuum_sim/config/vacuum_nav2.yaml').read_text())['collision_monitor']['ros__parameters'])
    p.update(cmd_vel_in_topic='/autonomy_guard_test/input',cmd_vel_out_topic='/autonomy_guard_test/output',
             state_topic='/autonomy_guard_test/state',polygons=['StopZone','SlowZone'])
    p['scan']['topic']='/autonomy_guard_test/scan'
    p['StopZone']['polygon_pub_topic']='/autonomy_guard_test/stop_polygon'
    p['SlowZone']['polygon_pub_topic']='/autonomy_guard_test/slow_polygon'
    guardfile=logs/'isolated_guard.yaml'
    guardfile.write_text(yaml.safe_dump({'/autonomy_guard_test/collision_monitor':{'ros__parameters':p}}))
    start('isolated_guard',['/opt/ros/jazzy/lib/nav2_collision_monitor/collision_monitor','--ros-args',
                           '-r','__ns:=/autonomy_guard_test','--params-file',str(guardfile)])
    service=node.create_client(ChangeState,'/autonomy_guard_test/collision_monitor/change_state')
    assert service.wait_for_service(timeout_sec=15),'Guard service unavailable'
    for transition in (1,3):
        request=ChangeState.Request()
        request.transition.id=transition
        future=service.call_async(request)
        assert wait(future.done,10) and future.result().success,'Guard lifecycle transition failed'
    outputs=[]
    subscriptions.append(node.create_subscription(Twist,'/autonomy_guard_test/output',outputs.append,10))
    command=node.create_publisher(Twist,'/autonomy_guard_test/input',10)
    scans=node.create_publisher(LaserScan,'/autonomy_guard_test/scan',qos_profile_sensor_data)
    def exercise(distance,seconds=1.5):
        start_count=len(outputs)
        started=time.monotonic()
        start_sim=node.get_clock().now().nanoseconds
        end=started+(15 if distance is None else seconds)
        next_pub=0
        while time.monotonic()<end:
            if distance is None and node.get_clock().now().nanoseconds-start_sim>1_500_000_000:
                break
            if time.monotonic()>=next_pub:
                twist=Twist(); twist.linear.x=.20
                command.publish(twist)
                if distance is not None:
                    scan=LaserScan()
                    scan.header.frame_id='base_footprint'
                    scan.header.stamp=node.get_clock().now().to_msg()
                    scan.angle_min=-.01; scan.angle_max=.01; scan.angle_increment=.01
                    scan.range_min=.08; scan.range_max=12.; scan.ranges=[distance]*3
                    scans.publish(scan)
                next_pub=time.monotonic()+.05
            rclpy.spin_once(node,timeout_sec=.02)
        assert len(outputs)>start_count,'Guard published no output'
        elapsed_sim=(node.get_clock().now().nanoseconds-start_sim)*1e-9
        print('guard phase',distance,'simulation seconds',elapsed_sim,'output',outputs[-1].linear.x,flush=True)
        if distance is None:
            assert elapsed_sim>1.0,'Simulator clock did not advance enough for source-timeout test'
        return outputs[-1].linear.x
    clear=exercise(float('inf'))
    slow=exercise(.30)
    stop=exercise(.18)
    # Make the preceding valid scan clear so stopping below proves data timeout.
    exercise(float('inf'))
    stale=exercise(None,2)
    assert abs(clear-.20)<.01 and abs(slow-.08)<.01 and abs(stop)<.001 and abs(stale)<.001,(clear,slow,stop,stale)
    result['tests']['isolated_guard']={'clear_m_s':clear,'slow_m_s':slow,'stop_m_s':stop,'scan_timeout_m_s':stale}
    result['passed']=True
    print(json.dumps(result,indent=2),flush=True)
except Exception as error:
    result['passed']=False
    result['error']=str(error)
    print(json.dumps(result,indent=2),flush=True)
    raise
finally:
    (logs/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    cleanup()
    node.destroy_node()
    rclpy.shutdown()


## tools/run_sim.py

#!/usr/bin/env python3
"""Run one simulator, retaining its lock until all owned child processes stop."""
import fcntl
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

workspace=Path(__file__).resolve().parents[1]
lock=(workspace/'.simulator.lock').open('a')
try:
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
except BlockingIOError:
    raise SystemExit('This workspace already has a simulator running. Stop its terminal first.')


def identity(pid,group):
    try:
        path=Path(f'/proc/{pid}')
        fields=(path/'stat').read_text().rsplit(')',1)[1].split()
        if fields[0]=='Z' or path.stat().st_uid!=os.getuid():return None
        if int(fields[2])!=group or int(fields[3])!=group:return None
        return fields[19]
    except (FileNotFoundError,ProcessLookupError,PermissionError):return None


def members(group):
    result={}
    for path in Path('/proc').iterdir():
        if path.name.isdigit():
            stamp=identity(path.name,group)
            if stamp is not None:result[int(path.name)]=stamp
    return result


def interrupted(signum,frame):raise KeyboardInterrupt
signal.signal(signal.SIGTERM,interrupted)
process=subprocess.Popen(['/bin/bash','-lc','source env.sh; exec "$@"','vacuum-launch',
                          'ros2','launch','vacuum_sim','sim.launch.py',*sys.argv[1:]],
                         cwd=workspace,start_new_session=True)
owned=members(process.pid)
result=0
try:
    while process.poll() is None:
        owned.update(members(process.pid))
        try:process.wait(timeout=.2)
        except subprocess.TimeoutExpired:pass
    result=process.returncode
except KeyboardInterrupt:result=130
finally:
    # Ignore repeat terminal signals while performing bounded cleanup.
    signal.signal(signal.SIGTERM,signal.SIG_IGN)
    signal.signal(signal.SIGINT,signal.SIG_IGN)
    if process.poll() is None:owned.update(members(process.pid))
    def active():
        return {pid:stamp for pid,stamp in owned.items() if identity(pid,process.pid)==stamp}
    for sig,seconds in ((signal.SIGINT,5),(signal.SIGTERM,4),(signal.SIGKILL,2)):
        if not active():break
        try:os.killpg(process.pid,sig)
        except ProcessLookupError:break
        deadline=time.monotonic()+seconds
        while active() and time.monotonic()<deadline:
            # Collect children while the original session leader is still alive.
            if process.poll() is None:owned.update(members(process.pid))
            time.sleep(.1)
    try:process.wait(timeout=1)
    except subprocess.TimeoutExpired:pass
    remaining=active()
    if remaining:
        print('Simulator cleanup incomplete; remaining owned PIDs: '+str(list(remaining)),file=sys.stderr)
        result=1
    lock.close()
sys.exit(result)


## tools/build_furnished_room.py

"""Build original, local room assets. Standard library only; no model downloads.



Meshes are batched by furniture item/material; physics uses simple proxies.

All dimensions are metres. Generated assets live inside the simulator package.

"""

from collections import defaultdict

import math

from pathlib import Path

import random

import struct

import xml.etree.ElementTree as ET

import zlib



PACKAGE = Path('/home/robot/vacuum_ws/src/vacuum_sim')

ASSETS = PACKAGE / 'worlds/furnished'

ASSETS.mkdir(parents=True, exist_ok=True)

DAE = 'http://www.collada.org/2005/11/COLLADASchema'





def png(name, size, pixel):

    width, height = size

    raw = bytearray()

    for y in range(height):

        raw.append(0)

        for x in range(width):

            raw.extend(max(0, min(255, int(v))) for v in pixel(x, y))

    def chunk(kind, data):

        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))

    (ASSETS / name).write_bytes(b'\x89PNG\r\n\x1a\n' +

        chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)) +

        chunk(b'IDAT', zlib.compress(bytes(raw), 7)) + chunk(b'IEND', b''))





def oak(x, y):

    plank = y // 48

    seam = y % 48 == 0 or (x + (plank % 3)*128) % 384 == 0

    if seam:

        return (132, 101, 68)

    grain = 5*math.sin(y*.65 + math.sin(x*.004)*4) + 2*math.sin(y*2+x*.015)

    shade = ((plank*17) % 13)-6 + grain + 2*math.sin(x*.03)

    return (181+shade, 139+shade, 94+shade*.7)





def fabric(x, y):

    grain = (x % 3 == 0)*7 - (y % 3 == 0)*5 + 2*math.sin(x*1.7+y*.8)

    return (184+grain, 169+grain, 145+grain)





def rug(x, y):

    edge = min(x, y, 511-x, 511-y)

    grain = ((x*7+y*13) % 11)-5

    stripe = edge < 12 or (22 < edge < 26) or (abs(x-256)+abs(y-256)) % 96 < 3

    return tuple(v+grain for v in ((65, 83, 86) if stripe else (201, 187, 157)))





def artwork(x, y):

    # An original abstract landscape, also used on the TV display.

    if (x-368)**2+(y-94)**2 < 37**2:

        return (239, 172, 102)

    if y > 194 + 31*math.sin(x*.009):

        return (42, 78, 83)

    if y > 150 + 38*math.sin(x*.011+1.4):

        return (71, 107, 112)

    return (174-y*.12, 199-y*.09, 204-y*.06)





def garden(x,y):

    if y > 275 + 22*math.sin(x*.009):return (102,126,73)

    if y > 244 + 18*math.sin(x*.014+.8):return (129,151,104)

    for cx,cy,r in ((80,212,90),(230,190,75),(710,200,110),(948,190,100)):

        if (x-cx)**2+(y-cy)**2<r*r:return (74+y*.09,112+y*.08,76+y*.05)

    cloud=math.exp(-((x-450)/180)**2-((y-86)/30)**2)+math.exp(-((x-750)/130)**2-((y-66)/22)**2)

    return (163+cloud*45+y*.06,196+cloud*25+y*.04,213+cloud*15)





png('oak.png', (2048, 2048), oak)

png('linen.png', (256, 256), fabric)

png('woven-rug.png', (512, 512), rug)

png('landscape.png', (512, 256), artwork)

png('garden.png', (1024,384), garden)



MATERIALS = {
    'aluminium': ((.62,.68,.75), None),
    'oak': ((.62, .43, .25), 'oak.png'),

    'linen': ((.73, .66, .55), 'linen.png'),

    'rug': ((.76, .71, .61), 'woven-rug.png'),

    'art': ((.5, .65, .7), 'landscape.png'),

    'garden': ((.7,.8,.7), 'garden.png'),

    'plaster': ((.86, .85, .80), None),

    'sage': ((.30, .42, .36), None),

    'white': ((.92, .90, .85), None),

    'teal': ((.16, .32, .34), None),

    'terra': ((.62, .27, .15), None),

    'brass': ((.63, .48, .24), None),

    'charcoal': ((.035, .045, .05), None),

    'ceramic': ((.77, .81, .77), None),

    'leaf': ((.10, .29, .11), None),

    'leaf_light': ((.22, .40, .16), None),

    'blue': ((.22, .35, .48), None),

    'burgundy': ((.40, .13, .17), None),

}





def rotate(point, yaw):

    x, y, z = point

    return (x*math.cos(yaw)-y*math.sin(yaw), x*math.sin(yaw)+y*math.cos(yaw), z)





class Mesh:

    def __init__(self):

        self.faces = defaultdict(list)



    def triangle(self, material, points, uvs=None, normals=None):

        if uvs is None:

            uvs = [(p[0]*2, p[1]*2+p[2]*2) for p in points]

        a, b, c = points

        u = tuple(b[i]-a[i] for i in range(3)); v = tuple(c[i]-a[i] for i in range(3))

        n = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])

        length = math.sqrt(sum(t*t for t in n))

        if length < 1e-10:

            return

        normal = tuple(t/length for t in n)

        self.faces[material].append((points, normals or [normal]*3, uvs))



    def quad(self, material, points, uvs=None, normals=None):

        if uvs is None:

            uvs = [(p[0]*2, p[1]*2+p[2]*2) for p in points]

        for indices in ((0, 1, 2), (0, 2, 3)):

            self.triangle(material, [points[i] for i in indices], [uvs[i] for i in indices],

                          [normals[i] for i in indices] if normals else None)



    def box(self, center, size, material, yaw=0, floor_uv=False):

        points = []

        for x, y, z in ((-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),

                        (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)):

            q = rotate((x*size[0]/2, y*size[1]/2, z*size[2]/2), yaw)

            points.append(tuple(q[i]+center[i] for i in range(3)))

        for face in ((0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)):

            p = [points[i] for i in face]

            uv = [((q[0]+8)/16,(q[1]+6)/12) for q in p] if floor_uv else None

            self.quad(material, p, uv)



    def rounded(self, center, size, radius, material, yaw=0):

        """Bevelled upholstered/wood parts: four rounded corners, curved edges."""

        sx, sy, sz = size

        radius = min(radius, sx/3, sy/3, sz/3)

        rings = []; normal_rings=[]

        for zsign, tilt in ((-1,-math.pi/2),(-1,-math.pi/3),(-1,-math.pi/6),(-1,0),

                            (1,0),(1,math.pi/6),(1,math.pi/3),(1,math.pi/2)):

            z=zsign*(sz/2-radius)+radius*math.sin(tilt)

            ring = []; normal_ring=[]

            for cx, cy, start in ((1,1,0),(-1,1,90),(-1,-1,180),(1,-1,270)):

                for j in range(5):

                    angle = math.radians(start+j*90/4)

                    r = max(.0001, radius*math.cos(tilt))

                    q = rotate((cx*(sx/2-radius)+r*math.cos(angle),

                                cy*(sy/2-radius)+r*math.sin(angle), z), yaw)

                    ring.append(tuple(q[i]+center[i] for i in range(3)))

                    normal_ring.append(rotate((math.cos(angle)*math.cos(tilt),math.sin(angle)*math.cos(tilt),math.sin(tilt)),yaw))

            rings.append(ring)

            normal_rings.append(normal_ring)

        count = len(rings[0])

        for layer,(lower, upper) in enumerate(zip(rings, rings[1:])):

            for j in range(count):

                k = (j+1) % count

                self.quad(material, [lower[j],lower[k],upper[k],upper[j]],

                          normals=[normal_rings[layer][j],normal_rings[layer][k],normal_rings[layer+1][k],normal_rings[layer+1][j]])

        for j in range(1,count-1):

            self.triangle(material, [rings[0][0],rings[0][j+1],rings[0][j]])

            self.triangle(material, [rings[-1][0],rings[-1][j],rings[-1][j+1]])



    def lathe(self, center, profile, material, segments=24):

        rings = [[(center[0]+r*math.cos(i*2*math.pi/segments),

                   center[1]+r*math.sin(i*2*math.pi/segments),center[2]+z)

                  for i in range(segments)] for r,z in profile]

        for lower,upper in zip(rings,rings[1:]):

            for i in range(segments):

                j=(i+1)%segments

                self.quad(material,[lower[i],lower[j],upper[j],upper[i]])

        for ring,reverse in ((rings[0],True),(rings[-1],False)):

            for i in range(1,segments-1):

                self.triangle(material,[ring[0],ring[i+1],ring[i]] if reverse else [ring[0],ring[i],ring[i+1]])



    def cylinder(self, center, radius, height, material):

        self.lathe(center,[(radius,-height/2),(radius,height/2)],material)



    def leaf(self, center, length, width, yaw, material):

        coords=[(0,0,0),(-width,length*.35,length*.22),(0,length*.5,length*.45),

                (width,length*.35,length*.22),(0,length*.85,length*.45)]

        p=[tuple(rotate(q,yaw)[i]+center[i] for i in range(3)) for q in coords]

        for face in ((0,1,2),(0,2,3),(1,4,2),(2,4,3)):

            self.triangle(material,[p[i] for i in face])

            self.triangle(material,[p[i] for i in reversed(face)])



    def save(self, name):

        root=ET.Element('COLLADA', xmlns=DAE, version='1.4.1')

        asset=ET.SubElement(root,'asset')

        ET.SubElement(asset,'unit',name='meter',meter='1')

        ET.SubElement(asset,'up_axis').text='Z_UP'

        images=ET.SubElement(root,'library_images'); effects=ET.SubElement(root,'library_effects')

        mats=ET.SubElement(root,'library_materials'); geometries=ET.SubElement(root,'library_geometries')

        scenes=ET.SubElement(root,'library_visual_scenes'); scene=ET.SubElement(scenes,'visual_scene',id='Scene',name='Scene')

        for mat,faces in self.faces.items():

            color,texture=MATERIALS[mat]

            effect=ET.SubElement(effects,'effect',id=mat+'fx'); profile=ET.SubElement(effect,'profile_COMMON')

            if texture:

                im=ET.SubElement(images,'image',id=mat+'image');ET.SubElement(im,'init_from').text=texture

                par=ET.SubElement(profile,'newparam',sid=mat+'surface'); surf=ET.SubElement(par,'surface',type='2D');ET.SubElement(surf,'init_from').text=mat+'image'

                par=ET.SubElement(profile,'newparam',sid=mat+'sampler');sample=ET.SubElement(par,'sampler2D');ET.SubElement(sample,'source').text=mat+'surface'

            phong=ET.SubElement(ET.SubElement(profile,'technique',sid='common'),'phong')

            ET.SubElement(ET.SubElement(phong,'ambient'),'color').text=' '.join(str(v*.7) for v in color)+' 1'

            diffuse=ET.SubElement(phong,'diffuse')

            if texture:ET.SubElement(diffuse,'texture',texture=mat+'sampler',texcoord='UVSET0')

            else:ET.SubElement(diffuse,'color').text=' '.join(map(str,color))+' 1'

            spec=.22 if mat=='brass' else .03

            ET.SubElement(ET.SubElement(phong,'specular'),'color').text=f'{spec} {spec} {spec} 1'

            ET.SubElement(ET.SubElement(phong,'shininess'),'float').text='20'

            material=ET.SubElement(mats,'material',id=mat,name=mat);ET.SubElement(material,'instance_effect',url='#'+mat+'fx')

            mesh=ET.SubElement(ET.SubElement(geometries,'geometry',id=mat+'mesh',name=mat),'mesh')

            positions=[];normals=[];uv=[]

            for points,ns,tex in faces:

                for p,t,n in zip(points,tex,ns): positions.extend(p);normals.extend(n);uv.extend(t)

            def source(sid,values,stride,params):

                src=ET.SubElement(mesh,'source',id=sid)

                ET.SubElement(src,'float_array',id=sid+'array',count=str(len(values))).text=' '.join(f'{v:.6f}' for v in values)

                accessor=ET.SubElement(ET.SubElement(src,'technique_common'),'accessor',source='#'+sid+'array',count=str(len(values)//stride),stride=str(stride))

                for param in params:ET.SubElement(accessor,'param',name=param,type='float')

            source(mat+'pos',positions,3,('X','Y','Z'));source(mat+'norm',normals,3,('X','Y','Z'));source(mat+'uv',uv,2,('S','T'))

            vertices=ET.SubElement(mesh,'vertices',id=mat+'verts');ET.SubElement(vertices,'input',semantic='POSITION',source='#'+mat+'pos')

            triangles=ET.SubElement(mesh,'triangles',material=mat,count=str(len(faces)))

            for semantic,src,offset in [('VERTEX',mat+'verts',0),('NORMAL',mat+'norm',1),('TEXCOORD',mat+'uv',2)]:

                ET.SubElement(triangles,'input',semantic=semantic,source='#'+src,offset=str(offset),**({'set':'0'} if offset==2 else {}))

            ET.SubElement(triangles,'p').text=' '.join(f'{i} {i} {i}' for i in range(len(positions)//3))

            node=ET.SubElement(scene,'node',id=mat+'node',name=mat,type='NODE')

            inst=ET.SubElement(node,'instance_geometry',url='#'+mat+'mesh')

            bind=ET.SubElement(ET.SubElement(inst,'bind_material'),'technique_common')

            im=ET.SubElement(bind,'instance_material',symbol=mat,target='#'+mat)

            ET.SubElement(im,'bind_vertex_input',semantic='UVSET0',input_semantic='TEXCOORD',input_set='0')

        ET.SubElement(ET.SubElement(root,'scene'),'instance_visual_scene',url='#Scene')

        path=ASSETS/(name+'.dae'); ET.ElementTree(root).write(path,encoding='utf-8',xml_declaration=True)

        return path





room_mesh = Mesh()

root=ET.Element('sdf',version='1.9');world=ET.SubElement(root,'world',name='vacuum_room')

def element(parent,tag,value):ET.SubElement(parent,tag).text=str(value)

physics=ET.SubElement(world,'physics',name='physics',type='ignored')

element(physics,'max_step_size','0.005555555555555556');element(physics,'real_time_factor',1.)

element(world,'gravity','0 0 -9.81')

for filename,classname in [('physics','Physics'),('user-commands','UserCommands'),('scene-broadcaster','SceneBroadcaster'),('sensors','Sensors')]:

    plugin=ET.SubElement(world,'plugin',filename='gz-sim-'+filename+'-system',name='gz::sim::systems::'+classname)

    if classname=='Sensors':element(plugin,'render_engine','ogre2')

scene=ET.SubElement(world,'scene');element(scene,'ambient','.7 .7 .7 1');element(scene,'background','.69 .79 .85 1');element(scene,'shadows','false')

light=ET.SubElement(world,'light',name='afternoon_daylight',type='directional')

element(light,'pose','0 0 6 0 0 0');element(light,'diffuse','.75 .72 .65 1');element(light,'specular','.15 .15 .15 1');element(light,'direction','-.5 -.4 -1');element(light,'cast_shadows','false')

light=ET.SubElement(world,'light',name='soft_window_fill',type='directional')

element(light,'pose','0 0 6 0 0 0');element(light,'diffuse','.25 .28 .3 1');element(light,'specular','0 0 0 1');element(light,'direction','.4 .4 -1');element(light,'cast_shadows','false')

gui=ET.SubElement(world,'gui',fullscreen='false')

# Main Gazebo window opens with a useful architectural view.

camera=ET.SubElement(gui,'camera',name='user_camera');element(camera,'pose','13 -16 13 0 .62 2.2')

room_model=ET.SubElement(world,'model',name='furnished_living_room');element(room_model,'static','true')

element(room_model,'self_collide','false')

room_link=ET.SubElement(room_model,'link',name='room')





class Item:

    def __init__(self,name,pose=(0,0,0,0)):

        self.name=name;self.mesh=Mesh();self.collisions=[];self.pose=pose

    def box(self,center,size,material,yaw=0,collision=False,rounded=0):

        if rounded:self.mesh.rounded(center,size,rounded,material,yaw)

        else:self.mesh.box(center,size,material,yaw)

        if collision:self.collisions.append(('box',center,size,yaw))

    def cylinder(self,center,radius,height,material,collision=False):

        self.mesh.cylinder(center,radius,height,material)

        if collision:self.collisions.append(('cylinder',center,(radius,height),0))

    def save(self):

        if self.name == 'architecture':

            # Enlarge only architecture, preserving human-scale furniture.

            for material, faces in self.mesh.faces.items():

                self.mesh.faces[material] = [([(p[0]*2, p[1]*12/7, p[2]) for p in points], normals, uvs)

                                            for points,normals,uvs in faces]

            self.collisions = [(kind,(c[0]*2,c[1]*12/7,c[2]),

                                (s[0]*2,s[1]*12/7,s[2]) if kind=='box' else s,yaw)

                               for kind,c,s,yaw in self.collisions]

        # One shared visual mesh gives the renderer one draw batch per material,

        # rather than repeating material/draw setup for each piece of furniture.

        x,y,z,yaw=self.pose

        for material,faces in self.mesh.faces.items():

            for points,normals,uvs in faces:

                transformed=[]

                for point in points:

                    q=rotate(point,yaw);transformed.append((q[0]+x,q[1]+y,q[2]+z))

                room_mesh.faces[material].append((transformed,[rotate(n,yaw) for n in normals],uvs))

        # All fixed furnishings are shapes of one immobile body. This prevents

        # expensive contact checks between the floor and static furniture.

        for i,(kind,center,size,local_yaw) in enumerate(self.collisions):

            q=rotate(center,yaw);center=(q[0]+x,q[1]+y,q[2]+z)

            collision=ET.SubElement(room_link,'collision',name=self.name+'_proxy'+str(i));element(collision,'pose',' '.join(map(str,center))+f' 0 0 {yaw+local_yaw}')

            shape=ET.SubElement(ET.SubElement(collision,'geometry'),kind)

            if kind=='box':element(shape,'size',' '.join(map(str,size)))

            else:element(shape,'radius',size[0]);element(shape,'length',size[1])





house=Item('architecture')

house.mesh.box((0,0,-.04),(8.2,7.2,.08),'oak',floor_uv=True)

house.collisions.append(('box',(0,0,-.04),(8.2,7.2,.08),0))

# North wall has a real window opening. Collision proxies match the wall pieces.

for center,size in [((0,-3.5,1.4),(8.2,.12,2.8)),((-4,0,1.4),(.12,7,2.8)),((4,0,1.4),(.12,7,2.8)),

                    ((0,3.5,.45),(8.2,.12,.9)),((0,3.5,2.65),(8.2,.12,.3)),

                    ((-3.15,3.5,1.7),(1.9,.12,1.6)),((3.15,3.5,1.7),(1.9,.12,1.6))]:

    house.box(center,size,'sage' if center[0]==4 else 'plaster',collision=True)

for x in (-4,4):house.box((x*.985,0,.055),(.035,6.95,.11),'white')

for y in (-3.5,3.5):house.box((0,y*.985,.055),(7.95,.035,.11),'white')

for x in (-2.19,0,2.19):house.box((x,3.48,1.7),(.055,.15,1.6),'white')

for z in (.9,1.7,2.5):house.box((0,3.48,z),(4.45,.16,.055),'white')

house.box((0,3.35,.88),(4.65,.40,.055),'oak')

house.mesh.quad('garden',[(-2.20,3.62,.90),(2.20,3.62,.90),(2.20,3.62,2.50),(-2.20,3.62,2.50)],[(0,0),(1,0),(1,1),(0,1)])

# Curtains, hung above floor clearance, with visible folds.

for side in (-1,1):

    for i in range(12):house.cylinder((side*2.25+(i-5.5)*.025,3.28,1.6),.029,2.05,'linen')

house.box((-2.5,-3.425,1.04),(.94,.035,2.05),'oak')

house.box((-2.5,-3.395,1.04),(1.02,.025,2.13),'white')

house.box((-2.5,-3.36,1.04),(.90,.025,2.01),'oak')

house.cylinder((-2.18,-3.32,1.03),.025,.05,'brass')

house.save()



sofa=Item('three_seat_sofa',(-2.8,4.95,0,0))

sofa.box((0,0,.28),(2.55,.90,.30),'teal',collision=True,rounded=.06)

sofa.box((0,.36,.65),(2.55,.21,.75),'teal',collision=True,rounded=.045)

for x in (-1.21,1.21):sofa.box((x,-.03,.53),(.18,.87,.56),'teal',collision=True,rounded=.035)

for x in (-.77,0,.77):

    sofa.box((x,-.08,.49),(.72,.65,.18),'linen',rounded=.05)

    sofa.box((x,.24,.74),(.70,.15,.44),'teal',rounded=.04)

for x,y in ((-1.08,-.30),(1.08,-.30),(-1.08,.30),(1.08,.30)):

    sofa.cylinder((x,y,.09),.035,.18,'oak',collision=True)

for x,mat,yaw in ((-.94,'terra',.18),(.88,'linen',-.2)):

    sofa.box((x,.10,.72),(.38,.22,.38),mat,yaw=yaw,rounded=.06)

sofa.save()



carpet=Item('woven_living_room_rug',(-2.8,3.45,0,0))

# A flush decorative rug is deliberately not a raised lidar-invisible obstacle.

carpet.mesh.quad('rug',[(-1.6,-1.15,.002),(1.6,-1.15,.002),(1.6,1.15,.002),(-1.6,1.15,.002)],[(0,0),(1,0),(1,1),(0,1)])

carpet.save()



coffee=Item('rounded_coffee_table',(-2.8,3.65,0,0))

coffee.box((0,0,.40),(1.25,.63,.07),'oak',collision=True,rounded=.018)

for x in (-.47,.47):

    for y in (-.21,.21):coffee.cylinder((x,y,.20),.035,.40,'charcoal',collision=True)

coffee.box((-.20,0,.45),(.28,.20,.025),'burgundy')

coffee.box((-.18,.01,.47),(.25,.18,.022),'white')

coffee.mesh.lathe((.29,.02,.44),[(.045,0),(.048,.08),(.046,.085)],'ceramic')

coffee.save()



console=Item('oak_media_console',(7.55,3.3,0,0))

console.box((0,0,.35),(.45,2.05,.51),'oak',collision=True,rounded=.012)

for y in (-.67,0,.67):

    console.box((-.235,y,.35),(.02,.64,.42),'oak')

    console.box((-.251,y,.50),(.016,.16,.009),'brass')

for y in (-.82,.82):console.cylinder((0,y,.075),.035,.15,'charcoal',collision=True)

console.box((.05,0,1.37),(.04,1.65,.96),'charcoal')

console.mesh.quad('art',[(.025,.79,.93),(.025,-.79,.93),(.025,-.79,1.81),(.025,.79,1.81)],[(0,0),(1,0),(1,1),(0,1)])

for y in (-.88,.88):console.cylinder((0,y,.70),.045,.20,'charcoal')

console.save()



bookshelf=Item('bookcase',(-7.65,3.4,0,0))

bookshelf.box((.08,0,.105),(.42,1.20,.21),'oak',collision=True)

bookshelf.box((-.05,0,1.05),(.12,1.20,2.1),'oak',collision=True)

for y in (-.57,.57):bookshelf.box((.08,y,1.05),(.42,.045,2.1),'oak',collision=True)

for z in (.06,.50,.96,1.42,1.88,2.12):bookshelf.box((.08,0,z),(.42,1.2,.035),'oak',collision=True)

rng=random.Random(17)

for row,z in enumerate((.50,.96,1.42)):

    for i in range(12):

        y=-.48+i*.073; h=rng.uniform(.22,.34)

        bookshelf.box((.13,y,z+.018+h/2),(.22,.055,h),rng.choice(['terra','blue','burgundy','white','teal']))

bookshelf.mesh.lathe((.10,-.22,1.90),[(.065,0),(.08,.09),(.045,.23),(.035,.25)],'ceramic')

bookshelf.box((.15,.32,1.96),(.18,.25,.08),'linen')

bookshelf.save()



dining=Item('dining_table',(-4.2,-2.0,0,0))

dining.box((0,0,.76),(1.45,.88,.065),'oak',collision=True,rounded=.02)

for x in (-.58,.58):

    for y in (-.30,.30):dining.cylinder((x,y,.37),.045,.74,'oak',collision=True)

for x in (-.35,.35):

    dining.cylinder((x,0,.804),.14,.014,'ceramic')

dining.mesh.lathe((0,0,.80),[(.05,0),(.09,.07),(.055,.21)],'terra')

dining.save()



def chair(name,pose):

    item=Item(name,pose)

    item.box((0,0,.45),(.45,.45,.065),'linen',collision=True,rounded=.02)

    item.box((0,.195,.72),(.46,.065,.50),'oak',collision=True,rounded=.015)

    for x in (-.16,.16):

        for y in (-.16,.16):item.cylinder((x,y,.225),.025,.45,'oak',collision=True)

    item.save()

for n,x,y,yaw in [('north',-4.2,-1.23,math.pi),('south',-4.2,-2.78,0),('west',-5.27,-2.0,-math.pi/2),('east',-3.13,-2.0,math.pi/2)]:

    chair('dining_chair_'+n,(x,y,0,yaw))



desk=Item('home_office_desk',(5.7,-5.55,0,0))

desk.box((0,0,.76),(1.65,.65,.055),'oak',collision=True,rounded=.015)

for x in (-.70,.70):

    for y in (-.23,.23):desk.box((x,y,.37),(.045,.045,.74),'charcoal',collision=True)

desk.box((.0,-.17,1.10),(.67,.035,.40),'charcoal')

desk.mesh.quad('art',[(.30,-.149,.925),(-.30,-.149,.925),(-.30,-.149,1.275),(.30,-.149,1.275)],[(0,0),(1,0),(1,1),(0,1)])

desk.box((0,-.17,.90),(.04,.05,.24),'charcoal')

desk.box((0,-.10,.805),(.25,.20,.025),'charcoal')

desk.box((0,.09,.805),(.43,.14,.016),'charcoal')

for y in (-.04,.0,.04):

    for x in range(14):desk.box((-.19+x*.028,y+.08,.816),(.021,.022,.004),'white')

desk.box((.58,.04,.812),(.14,.18,.024),'blue',rounded=.007)

desk.save()

chair('office_chair',(5.7,-4.65,0,math.pi))



lamp=Item('floor_lamp',(-.9,4.95,0,0))

lamp.cylinder((0,0,.105),.20,.21,'charcoal',collision=True)

lamp.cylinder((0,0,.77),.018,1.5,'brass',collision=True)

lamp.mesh.lathe((0,0,1.40),[(.28,0),(.21,.36)],'linen')

lamp.save()



def plant(name,pose,height):

    item=Item(name,pose)

    item.mesh.lathe((0,0,0),[(.16,0),(.21,.32),(.22,.34),(.20,.36)],'terra')

    item.collisions.append(('cylinder',(0,0,.18),(.22,.36),0))

    item.cylinder((0,0,.34+height*.35),.012,height*.7,'oak')

    for i in range(22):

        angle=i*2.399; radius=.03+(i%4)*.035

        z=.33+(i%7)*height/9

        item.mesh.leaf((radius*math.cos(angle),radius*math.sin(angle),z),height*.43,.09,angle,'leaf' if i%2 else 'leaf_light')

    item.save()

plant('window_plant',(5.8,5.3,0,0),1.20)

plant('entry_plant',(-7.0,-5.25,0,0),.72)



art=Item('framed_wall_art',(1.3,-2.5,0,0))

for x in (-.75,.40):

    art.box((x,-3.42,1.70),(.78,.04,1.04),'oak')

    art.mesh.quad('art',[(x+.35,-3.39,1.22),(x-.35,-3.39,1.22),(x-.35,-3.39,2.18),(x+.35,-3.39,2.18)],[(0,0),(1,0),(1,1),(0,1)])

art.save()



# Kitchen cabinetry and island keep the new floor plan furnished, with wide

# central aisles for high-speed simulator tests.

kitchen=Item('kitchen_wall',(0,-5.65,0,0))

for x in (-2.0,-1.0,0,1.0,2.0):

    kitchen.box((x,0,.46),(.98,.60,.92),'white',collision=True)

    kitchen.box((x,.313,.46),(.91,.025,.78),'oak')

    kitchen.box((x,.335,.75),(.22,.012,.015),'brass')

kitchen.box((0,0,.95),(5.1,.65,.055),'charcoal',collision=True)

kitchen.box((1.1,0,.989),(.63,.46,.020),'aluminium')

for x in (-1.4,-1.0):

    for y in (-.12,.12):kitchen.cylinder((x,y,.99),.082,.015,'charcoal')

kitchen.save()

island=Item('kitchen_island',(1.3,-2.7,0,0))

island.box((0,0,.45),(1.9,.75,.90),'oak',collision=True)

island.box((0,0,.93),(2.1,.95,.055),'white',collision=True,rounded=.014)

island.mesh.lathe((.55,0,.965),[(.10,0),(.16,.07),(.13,.09)],'terra')

island.save()

chair('island_stool_left',(.75,-1.75,0,math.pi))

chair('island_stool_right',(1.9,-1.75,0,math.pi))

reading=Item('reading_lounge',(4.6,2.8,0,-.35))

reading.box((0,0,.26),(1.10,.87,.33),'teal',collision=True,rounded=.06)

reading.box((0,.32,.65),(1.10,.20,.62),'teal',collision=True,rounded=.04)

for x in (-.49,.49):reading.box((x,0,.5),(.14,.80,.40),'teal',collision=True,rounded=.03)

for x in (-.42,.42):

    for y in (-.3,.3):reading.cylinder((x,y,.065),.027,.13,'oak',collision=True)

reading.save()

sidetable=Item('reading_side_table',(5.6,2.6,0,0))

sidetable.cylinder((0,0,.49),.30,.055,'oak',collision=True)

sidetable.cylinder((0,0,.23),.045,.46,'charcoal',collision=True)

sidetable.mesh.lathe((0,0,.52),[(.055,0),(.065,.12),(.04,.21)],'ceramic')

sidetable.save()

plant('reading_plant',(6.7,1.55,0,0),1.0)

bench=Item('entry_bench',(-4.3,-5.6,0,0))

bench.box((0,0,.42),(1.4,.45,.14),'linen',collision=True,rounded=.025)

for x in (-.56,.56):bench.box((x,0,.19),(.045,.37,.38),'oak',collision=True)

bench.save()



path=room_mesh.save('living_room')

visual=ET.SubElement(room_link,'visual',name='furnished_room');geometry=ET.SubElement(visual,'geometry')

element(ET.SubElement(geometry,'mesh'),'uri',str(path));element(visual,'cast_shadows','false')



ET.indent(root,space='  ')

ET.ElementTree(root).write(PACKAGE/'worlds/room.sdf',encoding='utf-8',xml_declaration=True)

print(f'Furnished 16 x 12 m room: one fixed body, {len(room_link.findall("collision"))} collision shapes, batched materials.')



## tools/validate_directional_guard.py

"""Exercise the exact drive guard in an isolated namespace, with no motor output."""

import copy

import json

import math

from pathlib import Path

import subprocess

import time

import yaml

import rclpy

from rclpy.node import Node

from rclpy.parameter import Parameter

from rclpy.qos import qos_profile_sensor_data

from geometry_msgs.msg import Twist

from sensor_msgs.msg import LaserScan

from lifecycle_msgs.srv import ChangeState



WS=Path('/home/robot/vacuum_ws')

OUT=WS/'validation/furnished-20261007'

OUT.mkdir(parents=True,exist_ok=True)

p=copy.deepcopy(yaml.safe_load((WS/'.lab/drive-guard.yaml').read_text())['collision_monitor']['ros__parameters'])

p.update(cmd_vel_in_topic='/furnished_guard_test/input',cmd_vel_out_topic='/furnished_guard_test/output',state_topic='/furnished_guard_test/state')

p['scan']['topic']='/furnished_guard_test/scan'

for key in ('StopZone','SlowZone'):p[key]['polygon_pub_topic']='/furnished_guard_test/'+key

config=OUT/'isolated-guard.yaml'

config.write_text(yaml.safe_dump({'/furnished_guard_test/collision_monitor':{'ros__parameters':p}}))

rclpy.init()

node=Node('furnished_guard_validation',parameter_overrides=[Parameter('use_sim_time',value=True)])

outputs=[]

node.create_subscription(Twist,'/furnished_guard_test/output',outputs.append,10)

pub=node.create_publisher(Twist,'/furnished_guard_test/input',10)

scans=node.create_publisher(LaserScan,'/furnished_guard_test/scan',qos_profile_sensor_data)

service=node.create_client(ChangeState,'/furnished_guard_test/collision_monitor/change_state')

log=(OUT/'isolated-guard.log').open('w')

proc=subprocess.Popen(['/opt/ros/jazzy/lib/nav2_collision_monitor/collision_monitor','--ros-args','-r','__ns:=/furnished_guard_test','-r','tf:=/tf','-r','tf_static:=/tf_static','--params-file',str(config)],stdout=log,stderr=subprocess.STDOUT)
report={'scope':'isolated test topics; no robot command output','tests':{}}





def wait(predicate,seconds):

    end=time.monotonic()+seconds

    while not predicate() and time.monotonic()<end:rclpy.spin_once(node,timeout_sec=.03)

    assert predicate(),'Timed out'





def exercise(label,speed,distance,angle=0):

    first=len(outputs);start=node.get_clock().now().nanoseconds

    end=time.monotonic()+5

    while time.monotonic()<end:

        cmd=Twist();cmd.linear.x=speed;pub.publish(cmd)

        if distance is not None:

            scan=LaserScan();scan.header.frame_id='base_footprint';scan.header.stamp=node.get_clock().now().to_msg()

            scan.angle_min=angle-.005;scan.angle_max=angle+.005;scan.angle_increment=.005

            scan.range_min=.03;scan.range_max=12.;scan.ranges=[distance]*3;scans.publish(scan)

        next_pub=time.monotonic()+.05

        while time.monotonic()<next_pub:rclpy.spin_once(node,timeout_sec=.01)

        if node.get_clock().now().nanoseconds-start>1_300_000_000 and len(outputs)>first:break

    assert len(outputs)>first,'No guard output'

    value=outputs[-1].linear.x

    report['tests'][label]=value

    print(label,value,flush=True)

    return value





try:

    assert service.wait_for_service(timeout_sec=15),'Guard lifecycle unavailable'

    for id in (1,3):

        req=ChangeState.Request();req.transition.id=id

        future=service.call_async(req);wait(future.done,10)

        assert future.result().success,'Lifecycle transition failed'

    wait(lambda: node.get_clock().now().nanoseconds>0,5)

    assert abs(exercise('clear_fast_forward',1.5,float('inf'))-1.5)<.01

    assert abs(exercise('forward_slow_front',1.5,1.25)-.60)<.01

    assert abs(exercise('forward_stop_front',1.5,.50))<.001

    assert abs(exercise('reverse_away_from_front',-.9,.50)+.90)<.01

    assert abs(exercise('reverse_stop_rear',-.9,.50,math.pi))<.001

    assert abs(exercise('forward_away_from_rear',1.5,.50,math.pi)-1.50)<.01

    # Side point inside the padded body must block motion even when a directional

    # strip would miss it: the predictive footprint remains active.

    assert abs(exercise('padded_body_contact_stop',1.5,.14,math.pi/2))<.001

    exercise('clear_before_timeout',1.5,float('inf'))

    assert abs(exercise('stale_lidar_stop',1.5,None))<.001

    report['passed']=True

finally:

    proc.terminate()

    try:proc.wait(timeout=8)

    except subprocess.TimeoutExpired:proc.kill();proc.wait(timeout=2)

    log.close();node.destroy_node();rclpy.shutdown()

    (OUT/'directional-guard.json').write_text(json.dumps(report,indent=2)+'\n')

    print(json.dumps(report,indent=2),flush=True)



## tools/validate_drive.py

"""Check camera delivery and forward/reverse movement in a running drive session."""

import json

import math

from pathlib import Path

import subprocess

import struct

import time

import zlib

import rclpy

from rclpy.node import Node

from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import Image

from nav_msgs.msg import Odometry

from geometry_msgs.msg import Twist



WS = Path('/home/robot/vacuum_ws')

rclpy.init()

node = Node('vacuum_direct_drive_validation')

images = []

odom = []

timed_odom = []

commands = []

def receive_odom(message):

    odom.append(message); timed_odom.append((time.monotonic(), message))

node.create_subscription(Odometry, '/odom', receive_odom, qos_profile_sensor_data)

node.create_subscription(Twist, '/vacuum/selected_cmd_vel', commands.append, 10)

report = {'date': '2026-10-07', 'scope': 'simulator only', 'tests': {}}

bridge = None

latest_image = None





def remember_image(message):

    global latest_image

    latest_image = message

    images.append((time.monotonic(), message.header.stamp.sec + message.header.stamp.nanosec * 1e-9))





node.create_subscription(Image, '/camera/image_raw', remember_image, qos_profile_sensor_data)





def spin(seconds):

    end = time.monotonic() + seconds

    while time.monotonic() < end:

        rclpy.spin_once(node, timeout_sec=.03)





try:
    reset=subprocess.run(['gz','service','-s','/world/vacuum_room/set_pose',
                          '--reqtype','gz.msgs.Pose','--reptype','gz.msgs.Boolean','--timeout','5000',
                          '--req','name: "vacuum", position: {x: 0 y: 0 z: 0.015}, orientation: {w: 1}'],
                         capture_output=True,text=True,timeout=8)
    assert reset.returncode==0 and 'true' in reset.stdout, 'Could not reset the test pose: '+reset.stdout+reset.stderr
    # Let the renderer and WSLg viewer settle after cold-start shader creation.

    spin(12)

    assert len(images) > 100 and odom, 'Camera or odometry unavailable'

    capture = images[-180:]

    fps_sim = (len(capture)-1) / (capture[-1][1]-capture[0][1])

    fps_wall = (len(capture)-1) / (capture[-1][0]-capture[0][0])

    report['tests']['camera'] = {'target_fps': 60, 'simulation_fps': fps_sim, 'wall_fps': fps_wall, 'frames': len(capture)}

    assert 57 <= fps_sim <= 63, f'Camera simulation frequency was {fps_sim}'

    assert fps_wall >= 55, f'Camera delivery too slow: {fps_wall}'

    log = (WS / '.lab/drive-validation-bridge.log').open('w')

    bridge = subprocess.Popen(['python3', 'tools/controller_bridge.py'], cwd=WS, text=True,

                              stdin=subprocess.PIPE, stdout=log, stderr=subprocess.STDOUT)



    def exercise(speed, held, seconds):

        end = time.monotonic() + seconds

        while time.monotonic() < end:

            assert bridge.poll() is None, 'Input bridge exited'

            bridge.stdin.write(json.dumps({'v': speed, 'w': 0., 'enabled': held}) + '\n')

            bridge.stdin.flush()

            # Drain camera/odom/command callbacks faster than their combined
            # arrival rate so test-side queues do not inflate response times.
            for _ in range(10):
                rclpy.spin_once(node, timeout_sec=0.)
            time.sleep(.01)


    exercise(0., False, 4)

    for label, speed, seconds in (('forward', 1.50, 2), ('reverse', -.90, 3)):

        before = odom[-1].pose.pose

        q = before.orientation

        yaw = math.atan2(2*(q.w*q.z + q.x*q.y), 1-2*(q.y*q.y+q.z*q.z))

        first = len(odom)

        issued=time.monotonic()

        exercise(speed, True, seconds)

        after = odom[-1].pose.pose.position

        displacement = (after.x-before.position.x)*math.cos(yaw) + (after.y-before.position.y)*math.sin(yaw)

        assert displacement * (1 if speed > 0 else -1) > .06, f'{label} did not move as expected: {displacement}'

        velocities = [m.twist.twist.linear.x for m in odom[first:]]

        actual_speed = max(velocities) if speed > 0 else min(velocities)

        assert abs(actual_speed) >= abs(speed)*.85, f'{label} speed clipped: {actual_speed}'

        after_command=[(t,m) for t,m in timed_odom if t>=issued]

        reaction=next(t-issued for t,m in after_command if abs(m.twist.twist.linear.x)>=abs(speed)*.10)

        rise=next(t-issued for t,m in after_command if abs(m.twist.twist.linear.x)>=abs(speed)*.90)

        assert reaction < .25, f'{label} response delayed: {reaction}'

        assert rise < .50, f'{label} rise too slow: {rise}'

        report['tests'][label] = {'signed_displacement_m': displacement, 'peak_odometry_m_s': actual_speed,

                                  'first_10_percent_wall_s':reaction,'time_to_90_percent_wall_s':rise}

        neutral_at=time.monotonic()

        exercise(0., True, 1)

        stopping=next(t-neutral_at for t,m in timed_odom if t>=neutral_at and abs(m.twist.twist.linear.x)<.02)

        assert stopping < .5, f'Neutral stop too slow: {stopping}'

        report['tests'][label]['neutral_stop_wall_s']=stopping

        assert abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02

    report['tests']['neutral_stop_without_hold_button'] = True

    report['tests']['disarmed_stop'] = True

    exercise(0., False, .5)

    # A pure turn tests the smaller wheels and higher yaw command without a

    # translational goal or a held-button input.

    turn_start=time.monotonic()

    while time.monotonic()-turn_start<1.0:

        bridge.stdin.write(json.dumps({'v':0.,'w':2.4,'enabled':True})+'\n');bridge.stdin.flush()

        for _ in range(10):rclpy.spin_once(node,timeout_sec=0.)
        time.sleep(.01)
    turn_records=[(t,m) for t,m in timed_odom if t>=turn_start]

    peak=max(abs(m.twist.twist.angular.z) for t,m in turn_records)

    assert peak>2.0, f'Turn speed clipped: {peak}'

    turn_rise=next(t-turn_start for t,m in turn_records if abs(m.twist.twist.angular.z)>=2.16)

    assert turn_rise<.5, f'Turn rise too slow: {turn_rise}'

    report['tests']['steering']={'peak_rad_s':peak,'time_to_90_percent_wall_s':turn_rise}

    exercise(0.,False,1)

    exercise(.2, True, 1)

    spin(2)

    assert abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02

    report['tests']['input_timeout_stop'] = True

    message = latest_image

    assert message.encoding in ('rgb8','bgr8'), message.encoding

    rows = []

    data = bytes(message.data)

    for y in range(message.height):

        row = data[y*message.step:y*message.step+message.width*3]

        if message.encoding == 'bgr8':

            row = bytes(v for i in range(0,len(row),3) for v in (row[i+2],row[i+1],row[i]))

        rows.append(b'\0'+row)

    def chunk(kind, content):

        return struct.pack('>I',len(content))+kind+content+struct.pack('>I',zlib.crc32(kind+content))

    png = b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',message.width,message.height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b''.join(rows)))+chunk(b'IEND',b'')

    (WS/'validation/furnished-robot-camera.png').write_bytes(png)

    report['passed'] = True

except Exception as exc:

    report['passed'] = False

    report['error'] = str(exc)

    raise

finally:

    if bridge:

        try:

            bridge.stdin.close()

            bridge.wait(timeout=5)

        except Exception:

            bridge.terminate()

    path = WS / 'validation/modern-drive-20261007'

    path.mkdir(parents=True, exist_ok=True)

    (path / 'results.json').write_text(json.dumps(report, indent=2) + '\n')

    print(json.dumps(report, indent=2), flush=True)

    node.destroy_node()

    rclpy.shutdown()



## tools/capture_room_preview.py

"""Temporarily add a camera to the running simulator and save a room overview."""

from pathlib import Path

import struct

import subprocess

import time

import zlib

import rclpy

from rclpy.node import Node

from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import Image



WS=Path('/home/robot/vacuum_ws')

out=WS/'validation/furnished-20261007';out.mkdir(parents=True,exist_ok=True)

sdf=out/'preview-camera.sdf'

sdf.write_text('''<sdf version="1.9"><model name="room_preview"><static>true</static>

<pose>-12.0 -10.0 20.0 0 0.91 0.695</pose><link name="camera">
<sensor name="overview" type="camera"><topic>/room_preview</topic><always_on>true</always_on><update_rate>1</update_rate>

<camera><horizontal_fov>1.1</horizontal_fov><image><width>1200</width><height>900</height><format>R8G8B8</format></image>
<clip><near>0.05</near><far>45</far></clip></camera></sensor></link></model></sdf>''')

rclpy.init();node=Node('furnished_room_preview_capture');images=[]

node.create_subscription(Image,'/room_preview',images.append,qos_profile_sensor_data)

bridge=None

created=False

try:

    result=subprocess.run(['/opt/ros/jazzy/lib/ros_gz_sim/create','-world','vacuum_room','-file',str(sdf),'-name','room_preview',

                           '-x','-12','-y','-10','-z','20','-R','0','-P','.91','-Y','.695'],capture_output=True,text=True,timeout=20)
    assert result.returncode==0,result.stdout+result.stderr

    created=True

    log=(out/'preview-bridge.log').open('w')

    bridge=subprocess.Popen(['/opt/ros/jazzy/lib/ros_gz_bridge/parameter_bridge','/room_preview@sensor_msgs/msg/Image[gz.msgs.Image'],stdout=log,stderr=subprocess.STDOUT)

    end=time.monotonic()+25

    while not images and time.monotonic()<end:rclpy.spin_once(node,timeout_sec=.1)

    assert images,'Preview camera did not publish'

    m=images[-1];assert m.encoding=='rgb8',m.encoding

    data=bytes(m.data);raw=b''.join(b'\0'+data[y*m.step:y*m.step+m.width*3] for y in range(m.height))

    def chunk(kind,data):return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data))

    png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',m.width,m.height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b'')

    path=out/'room-overview.png';path.write_bytes(png);print(path,flush=True)

finally:

    if bridge:

        bridge.terminate()

        try:bridge.wait(timeout=5)

        except subprocess.TimeoutExpired:bridge.kill();bridge.wait(timeout=2)

        log.close()

    if created:

        result=subprocess.run(['gz','service','-s','/world/vacuum_room/remove','--reqtype','gz.msgs.Entity','--reptype','gz.msgs.Boolean','--timeout','5000','--req','name: "room_preview", type: MODEL'],capture_output=True,text=True,timeout=8)

        print('Preview camera removal:',result.stdout.strip(),result.stderr.strip(),flush=True)

    node.destroy_node();rclpy.shutdown()



## tools/capture_robot_preview.py

"""Temporarily add a camera to the running simulator and save a room overview."""

from pathlib import Path

import struct

import subprocess

import time

import zlib

import rclpy

from rclpy.node import Node

from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import Image



WS=Path('/home/robot/vacuum_ws')

out=WS/'validation/furnished-20261007';out.mkdir(parents=True,exist_ok=True)

sdf=out/'preview-camera.sdf'

sdf.write_text('''<sdf version="1.9"><model name="robot_preview"><static>true</static>

<pose>.4 -.42 .19 0 .17 2.332</pose><link name="camera">

<sensor name="overview" type="camera"><topic>/robot_preview</topic><always_on>true</always_on><update_rate>1</update_rate>

<camera><horizontal_fov>1.0</horizontal_fov><image><width>1400</width><height>850</height><format>R8G8B8</format></image>

<clip><near>0.05</near><far>45</far></clip></camera></sensor></link></model></sdf>''')

rclpy.init();node=Node('furnished_robot_preview_capture');images=[]

node.create_subscription(Image,'/robot_preview',images.append,qos_profile_sensor_data)

bridge=None

created=False

try:

    reset=subprocess.run(['gz','service','-s','/world/vacuum_room/set_pose',

                         '--reqtype','gz.msgs.Pose','--reptype','gz.msgs.Boolean','--timeout','5000',

                         '--req','name: "vacuum", position: {x: 0 y: 0 z: 0.015}, orientation: {w: 1}'],

                         capture_output=True,text=True,timeout=8)

    assert reset.returncode==0 and 'true' in reset.stdout,reset.stdout+reset.stderr

    time.sleep(1)

    result=subprocess.run(['/opt/ros/jazzy/lib/ros_gz_sim/create','-world','vacuum_room','-file',str(sdf),'-name','robot_preview',

                           '-x','.4','-y','-.42','-z','.19','-R','0','-P','.17','-Y','2.332'],capture_output=True,text=True,timeout=20)
    assert result.returncode==0,result.stdout+result.stderr

    created=True

    log=(out/'preview-bridge.log').open('w')

    bridge=subprocess.Popen(['/opt/ros/jazzy/lib/ros_gz_bridge/parameter_bridge','/robot_preview@sensor_msgs/msg/Image[gz.msgs.Image'],stdout=log,stderr=subprocess.STDOUT)

    end=time.monotonic()+25

    while not images and time.monotonic()<end:rclpy.spin_once(node,timeout_sec=.1)

    assert images,'Preview camera did not publish'

    m=images[-1];assert m.encoding=='rgb8',m.encoding

    data=bytes(m.data);raw=b''.join(b'\0'+data[y*m.step:y*m.step+m.width*3] for y in range(m.height))

    def chunk(kind,data):return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data))

    png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',m.width,m.height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b'')

    path=out/'robot-hardware.png';path.write_bytes(png);print(path,flush=True)

finally:

    if bridge:

        bridge.terminate()

        try:bridge.wait(timeout=5)

        except subprocess.TimeoutExpired:bridge.kill();bridge.wait(timeout=2)

        log.close()

    if created:

        result=subprocess.run(['gz','service','-s','/world/vacuum_room/remove','--reqtype','gz.msgs.Entity','--reptype','gz.msgs.Boolean','--timeout','5000','--req','name: "robot_preview", type: MODEL'],capture_output=True,text=True,timeout=8)

        print('Preview camera removal:',result.stdout.strip(),result.stderr.strip(),flush=True)

    node.destroy_node();rclpy.shutdown()



## tools/check_lab.py

"""Logic checks using installed ROS types; does not move the robot."""

import math

from pathlib import Path

import tempfile

import threading

import time

from types import SimpleNamespace

import unittest

from geometry_msgs.msg import Twist

import command_gate

import controller_bridge

from prepare_lab import circle





class Publisher:

    def __init__(self):

        self.messages = []



    def publish(self, message):

        self.messages.append(message)





class SafetyTests(unittest.TestCase):

    def test_decode(self):

        self.assertEqual(controller_bridge.decode('{"v":100,"w":100,"held":true}'), (1.50, 2.4))

        self.assertEqual(controller_bridge.decode('{"v":-100,"w":-100,"held":true}'), (-.90, -2.4))

        self.assertEqual(controller_bridge.decode('{"v":0.1,"w":0.2,"held":false}'), (0., 0.))

        with self.assertRaises(ValueError):

            controller_bridge.decode('{"v":"NaN","w":0,"held":true}')



    def test_armed_input_without_hold_button(self):

        self.assertEqual(controller_bridge.decode('{"v":1.5,"w":2.4,"enabled":true}'), (1.5, 2.4))

        self.assertEqual(controller_bridge.decode('{"v":1.5,"w":0,"enabled":false}'), (0., 0.))

        self.assertEqual(controller_bridge.decode('{"v":1.5,"w":0}'), (0., 0.))



    def test_manual_watchdog_and_interlock(self):

        from unittest.mock import patch

        fake = SimpleNamespace(pub=Publisher(), lock=threading.Lock(), latest=(.15, .5),

                               received=time.monotonic(), closed=False,

                               states={'collision_monitor': (3, time.monotonic())},

                               scan_at=time.monotonic(), motion_since=0.,

                               report=lambda *args: None)

        with patch.object(controller_bridge, 'MODE') as mode:

            mode.exists.return_value = True

            controller_bridge.Bridge.tick(fake)

            self.assertEqual(fake.pub.messages[-1].linear.x, .15)

            mode.exists.return_value = False

            controller_bridge.Bridge.tick(fake)

            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)

            mode.exists.return_value = True

            fake.received = time.monotonic() - .5

            controller_bridge.Bridge.tick(fake)

            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)

            fake.received = time.monotonic()

            fake.states['collision_monitor'] = (3, time.monotonic() - 2.)

            controller_bridge.Bridge.tick(fake)

            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)

            fake.states['collision_monitor'] = (3, time.monotonic())

            fake.scan_at = time.monotonic() - .6

            controller_bridge.Bridge.tick(fake)

            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)



    def test_gate_mode_and_timeout(self):

        root = Path('/home/robot/vacuum_ws/.lab')

        root.mkdir(exist_ok=True)

        with tempfile.TemporaryDirectory(dir=root) as folder:

            previous = command_gate.MODE

            command_gate.MODE = Path(folder) / 'manual'

            fake = SimpleNamespace(pub=Publisher(), mode='auto', inputs={'auto': (0.,0.,0.), 'manual': (0.,0.,0.)},

                                   last_status=None, get_logger=lambda: SimpleNamespace(info=lambda msg: None))

            try:

                auto = Twist(); auto.linear.x = .2

                command_gate.Gate.receive(fake, 'auto', auto)

                command_gate.Gate.tick(fake)

                self.assertEqual(fake.pub.messages[-1].linear.x, .2)

                command_gate.MODE.touch()

                command_gate.Gate.tick(fake)

                self.assertEqual(fake.pub.messages[-1].linear.x, 0.)

                command_gate.Gate.receive(fake, 'auto', auto)

                command_gate.Gate.tick(fake)

                self.assertEqual(fake.pub.messages[-1].linear.x, 0.)

                manual = Twist(); manual.linear.x = .1

                command_gate.Gate.receive(fake, 'manual', manual)

                command_gate.Gate.tick(fake)

                self.assertEqual(fake.pub.messages[-1].linear.x, .1)

                fake.inputs['manual'] = (.1, 0., time.monotonic() - .5)

                command_gate.Gate.tick(fake)

                self.assertEqual(fake.pub.messages[-1].linear.x, 0.)

            finally:

                command_gate.MODE = previous



    def test_health_check_recovers_from_lost_response(self):

        from concurrent.futures import Future

        lost, replacement = Future(), Future()

        removed = []

        client = SimpleNamespace(service_is_ready=lambda: True,

                                 remove_pending_request=removed.append,

                                 call_async=lambda request: replacement)

        fake = SimpleNamespace(state_clients={'collision_monitor': client},

                               pending={'collision_monitor': (lost, time.monotonic()-1)},

                               record=lambda *args: None)

        controller_bridge.Bridge.check_states(fake)

        self.assertTrue(lost.cancelled())

        self.assertEqual(removed, [lost])

        self.assertIs(fake.pending['collision_monitor'][0], replacement)



    def test_circular_footprint_and_wheel_envelope(self):

        points = circle(.15)

        for a, b in zip(points, points[1:] + points[:1]):

            ax, ay = a[0]+.03, a[1]

            bx, by = b[0]+.03, b[1]

            distance = abs(ax*by-ay*bx) / math.hypot(bx-ax, by-ay)

            self.assertGreaterEqual(distance, .15 - 1e-6)

        self.assertLess(math.hypot(.03+.05, .22/2+.025/2), .15)





if __name__ == '__main__':

    unittest.main()



## tools/robot-profile.json

{
  "version": 2,
  "scope": "simulation",
  "hardware": {
    "drive_motors": "2 x NEMA 17, mounted beneath the chassis",
    "stepper_drivers": "2 x TB6600 modules",
    "microcontroller": "Arduino Mega 2560",
    "computer": "Orange Pi 5",
    "lidar": "RPLIDAR C1",
    "wheel_diameter_m": 0.07,
    "wheel_separation_m": 0.22,
    "chassis_diameter_m": 0.30,
    "motor_body_m": [0.0423, 0.040, 0.0423],
    "estimated_geometry": "Motor length, driver enclosure, mount height, mass and chassis layout are provisional; exact motor/driver variants were not supplied."
  },
  "drive": {
    "forward_m_s": 1.5,
    "reverse_m_s": 0.9,
    "turn_rad_s": 2.4,
    "acceleration_m_s2": 6.0,
    "angular_acceleration_rad_s2": 14.0,
    "input_period_s": 0.02,
    "odometry_window_samples": 3,
    "require_hold_button": false
  },
  "room": {"width_m": 16.0, "depth_m": 12.0},
  "lidar": {"min_range_m": 0.05, "max_range_m": 12.0, "scan_hz": 10.0, "samples": 500, "serial_baud": 460800}
}


## tools/prepare_nav2.py

#!/usr/bin/env python3
"""Adapt the installed Jazzy Nav2 defaults; run in Ubuntu before colcon build.

Keeping defaults from the installed package avoids inventing plugin names or
dropping lifecycle nodes introduced in package updates. Review the generated YAML.
"""
from pathlib import Path
import yaml

workspace = Path(__file__).resolve().parents[1]
source = Path('/opt/ros/jazzy/share/nav2_bringup/params/nav2_params.yaml')
target = workspace / 'src/vacuum_sim/config/nav2.yaml'
if target.exists():
    raise SystemExit(f'{target} already exists; preserve and review existing configuration.')
data = yaml.safe_load(source.read_text())


def set_sim_time(value):
    if isinstance(value, dict):
        if 'ros__parameters' in value:
            value['ros__parameters']['use_sim_time'] = True
        for item in value.values():
            set_sim_time(item)


set_sim_time(data)
for name in ('bt_navigator', 'behavior_server'):
    params = data[name]['ros__parameters']
    params['robot_base_frame'] = 'base_footprint'
    params['odom_topic'] = '/odom'
    params['enable_stamped_cmd_vel'] = False

for name in ('local_costmap', 'global_costmap'):
    params = data[name][name]['ros__parameters']
    params['robot_base_frame'] = 'base_footprint'
    params['robot_radius'] = 0.22
    params.pop('footprint', None)
    params['resolution'] = 0.05
    params['inflation_layer']['inflation_radius'] = 0.35
    for layer in ('voxel_layer', 'obstacle_layer'):
        if layer in params and 'scan' in params[layer]:
            params[layer]['scan'].update(topic='/scan', data_type='LaserScan',
                                        obstacle_max_range=6.0, raytrace_max_range=8.0)

controller = data['controller_server']['ros__parameters']
controller['controller_frequency'] = 20.0
controller['odom_topic'] = '/odom'
controller['enable_stamped_cmd_vel'] = False
controller['progress_checker'].update(required_movement_radius=0.15, movement_time_allowance=30.0)
controller['general_goal_checker'].update(xy_goal_tolerance=0.15, yaw_goal_tolerance=0.25)
controller['controller_plugins'] = ['FollowPath']
controller['FollowPath'] = {
    'plugin': 'dwb_core::DWBLocalPlanner',
    'debug_trajectory_details': False,
    'min_vel_x': -0.15, 'max_vel_x': 0.25,
    'min_vel_y': 0.0, 'max_vel_y': 0.0,
    'max_vel_theta': 1.0,
    'min_speed_xy': 0.0, 'max_speed_xy': 0.25, 'min_speed_theta': 0.0,
    'acc_lim_x': 0.3, 'acc_lim_y': 0.0, 'acc_lim_theta': 1.0,
    'decel_lim_x': -0.3, 'decel_lim_y': 0.0, 'decel_lim_theta': -1.0,
    'vx_samples': 20, 'vy_samples': 1, 'vtheta_samples': 20,
    'sim_time': 1.7, 'linear_granularity': 0.05, 'angular_granularity': 0.025,
    'transform_tolerance': 0.2, 'xy_goal_tolerance': 0.15,
    'trans_stopped_velocity': 0.02, 'short_circuit_trajectory_evaluation': True,
    'stateful': True,
    'critics': ['RotateToGoal', 'Oscillation', 'BaseObstacle', 'GoalAlign', 'PathAlign', 'PathDist', 'GoalDist'],
    'BaseObstacle.scale': 0.02,
    'PathAlign.scale': 32.0, 'PathAlign.forward_point_distance': 0.1,
    'GoalAlign.scale': 24.0, 'GoalAlign.forward_point_distance': 0.1,
    'PathDist.scale': 32.0, 'GoalDist.scale': 24.0,
    'RotateToGoal.scale': 32.0, 'RotateToGoal.slowing_factor': 5.0,
    'RotateToGoal.lookahead_time': -1.0,
}
if 'velocity_smoother' in data:
    data['velocity_smoother']['ros__parameters'].update(
        enable_stamped_cmd_vel=False,
        max_velocity=[0.25, 0.0, 1.0], min_velocity=[-0.15, 0.0, -1.0],
        max_accel=[0.3, 0.0, 1.0], max_decel=[-0.3, 0.0, -1.0],
        odom_topic='/odom', feedback='OPEN_LOOP', velocity_timeout=0.5)
if 'collision_monitor' in data:
    data['collision_monitor']['ros__parameters'].update(enable_stamped_cmd_vel=False,
        base_frame_id='base_footprint', cmd_vel_in_topic='cmd_vel_smoothed', cmd_vel_out_topic='cmd_vel')
if 'docking_server' in data:
    data['docking_server']['ros__parameters'].update(enable_stamped_cmd_vel=False, base_frame='base_footprint')
data['planner_server']['ros__parameters']['GridBased']['allow_unknown'] = False
target.write_text(yaml.safe_dump(data, sort_keys=False))
print(f'Prepared {target}; navigation runtime validation remains required.')


## tools/command_gate.py

"""Select exactly one launcher command source before Collision Monitor."""

import math

from pathlib import Path

import json

import time

import rclpy

from geometry_msgs.msg import Twist

from rclpy.node import Node



MODE = Path('/home/robot/vacuum_ws/.lab/manual-mode')

PROFILE = json.loads((Path(__file__).parent / 'robot-profile.json').read_text())['drive']





class Gate(Node):

    def __init__(self):

        super().__init__('vacuum_command_gate')

        self.pub = self.create_publisher(Twist, '/vacuum/selected_cmd_vel', 1)

        self.inputs = {'manual': (0., 0., 0.), 'auto': (0., 0., 0.)}

        self.mode = 'manual' if MODE.exists() else 'auto'

        self.last_status = None

        self.create_subscription(Twist, '/cmd_vel_smoothed', lambda msg: self.receive('auto', msg), 1)

        self.create_subscription(Twist, '/vacuum/manual_cmd_vel', lambda msg: self.receive('manual', msg), 1)

        self.create_timer(PROFILE['input_period_s'], self.tick)



    def receive(self, source, msg):

        v, w = msg.linear.x, msg.angular.z

        if not math.isfinite(v) or not math.isfinite(w):

            v, w = 0., 0.

        self.inputs[source] = (max(-PROFILE['reverse_m_s'], min(PROFILE['forward_m_s'], v)), max(-PROFILE['turn_rad_s'], min(PROFILE['turn_rad_s'], w)), time.monotonic())



    def tick(self):

        mode = 'manual' if MODE.exists() else 'auto'

        if mode != self.mode:

            self.mode = mode

            # Require fresh input after every mode transition.

            self.inputs = {'manual': (0., 0., 0.), 'auto': (0., 0., 0.)}

        v, w, stamp = self.inputs[mode]

        message = Twist()

        if time.monotonic() - stamp < .3:

            message.linear.x, message.angular.z = v, w

        status = (mode, abs(message.linear.x) > .001 or abs(message.angular.z) > .001)

        if status != self.last_status:

            self.get_logger().info(f'Selected {mode}: speed={message.linear.x:.3f}, turn={message.angular.z:.3f}')

            self.last_status = status

        self.pub.publish(message)





def main():

    rclpy.init()

    node = Gate()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:

        pass

    finally:

        node.pub.publish(Twist())

        node.destroy_node()

        if rclpy.ok():

            rclpy.shutdown()





if __name__ == '__main__':

    main()



## maps

## maps/room-20261007-205305-599814.yaml

image: room-20261007-205305-599814.pgm
mode: trinary
resolution: 0.050
origin: [-2.967, -2.973, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

## maps/room-20261007-205732-316107.yaml

image: room-20261007-205732-316107.pgm
mode: trinary
resolution: 0.050
origin: [-2.972, -2.979, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

## maps/room.pgm

## maps/room-20261007-235926-520113.pgm

## maps/room-20261007-210454-328329.pgm

## maps/room-20261007-205732-316107.pgm

## maps/room-20261007-205305-599814.pgm

## maps/room-20261007-210454-328329.yaml

image: room-20261007-210454-328329.pgm
mode: trinary
resolution: 0.050
origin: [-2.979, -2.974, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

## maps/room-20261007-204953-160957.pgm

## maps/room-20261007-210137-532422.pgm

## maps/room.yaml

image: room.pgm
mode: trinary
resolution: 0.050
origin: [-2.966, -2.974, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

## maps/room-20261007-205925-376184.pgm

## maps/room-20261007-224435-484972.pgm

## maps/room-20261007-204953-160957.yaml

image: room-20261007-204953-160957.pgm
mode: trinary
resolution: 0.050
origin: [-2.967, -2.973, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

## maps/room-20261007-235926-520113.yaml

image: room-20261007-235926-520113.pgm
mode: trinary
resolution: 0.050
origin: [-7.931, -5.944, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

## maps/room-20261007-205925-376184.yaml

image: room-20261007-205925-376184.pgm
mode: trinary
resolution: 0.050
origin: [-2.972, -2.979, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

## maps/room-20261007-224435-484972.yaml

image: room-20261007-224435-484972.pgm
mode: trinary
resolution: 0.050
origin: [-3.960, -3.464, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

## maps/room-20261007-210137-532422.yaml

image: room-20261007-210137-532422.pgm
mode: trinary
resolution: 0.050
origin: [-2.972, -2.979, 0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196

## validation

## validation/mapping.log

[INFO] [launch]: All log files can be found below /home/robot/.ros/log/2026-09-30-22-19-41-193720-Justin-843
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [async_slam_toolbox_node-1]: process started with pid [921]
[async_slam_toolbox_node-1] [INFO] [1790777982.916504610] [slam_toolbox]: Configuring
[async_slam_toolbox_node-1] [INFO] [1790777982.966260893] [slam_toolbox]: Using solver plugin solver_plugins::CeresSolver
[async_slam_toolbox_node-1] [INFO] [1790777982.966732564] [slam_toolbox]: CeresSolver: Using SCHUR_JACOBI preconditioner.
[INFO] [launch.user]: [LifecycleLaunch] Slamtoolbox node is activating.
[async_slam_toolbox_node-1] [INFO] [1790777983.056904245] [slam_toolbox]: Activating
[async_slam_toolbox_node-1] Registering sensor: [Custom Described Lidar]
[async_slam_toolbox_node-1] [INFO] [1790778332.210711867] [slam_toolbox]: Message Filter dropping message: frame 'lidar_link' at time 1236.400 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[INFO] [async_slam_toolbox_node-1]: sending signal 'SIGINT' to process[async_slam_toolbox_node-1]
[async_slam_toolbox_node-1] [INFO] [1790778340.167571392] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[async_slam_toolbox_node-1] Unregistering sensor: Custom Described Lidar
[INFO] [async_slam_toolbox_node-1]: process has finished cleanly [pid 921]


## validation/sim.pid

## validation/mapping.pid

## validation/sim.log

[INFO] [launch]: All log files can be found below /home/robot/.ros/log/2026-09-30-23-43-02-424790-Justin-1261
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [gz-1]: process started with pid [1287]
[INFO] [gz-2]: process started with pid [1288]
[INFO] [robot_state_publisher-3]: process started with pid [1289]
[INFO] [parameter_bridge-4]: process started with pid [1290]
[INFO] [create-5]: process started with pid [1291]
[INFO] [twist_adapter.py-6]: process started with pid [1292]
[INFO] [rviz2-7]: process started with pid [1293]
[robot_state_publisher-3] [INFO] [1790782982.684651227] [robot_state_publisher]: Robot initialized
[create-5] [INFO] [1790782982.696559721] [ros_gz_sim]: Waiting messages on topic [/robot_description].
[create-5] [INFO] [1790782983.239466832] [ros_gz_sim]: Entity creation successful.
[INFO] [create-5]: process has finished cleanly [pid 1291]
[INFO] [spawner-8]: process started with pid [1408]
[parameter_bridge-4] [INFO] [1790782983.718306703] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/clock (gz.msgs.Clock) -> /clock (rosgraph_msgs/msg/Clock)] (Lazy 0)
[parameter_bridge-4] [INFO] [1790782983.720770444] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/scan (gz.msgs.LaserScan) -> /scan (sensor_msgs/msg/LaserScan)] (Lazy 0)
[parameter_bridge-4] [INFO] [1790782983.726280497] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/camera/image_raw (gz.msgs.Image) -> /camera/image_raw (sensor_msgs/msg/Image)] (Lazy 0)
[parameter_bridge-4] [INFO] [1790782983.727816469] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/camera/camera_info (gz.msgs.CameraInfo) -> /camera/camera_info (sensor_msgs/msg/CameraInfo)] (Lazy 0)
[spawner-8] [INFO] [1790782984.036261674] [spawner_joint_state_broadcaster]: waiting for service /controller_manager/list_controllers to become available...
[rviz2-7] [INFO] [1790782984.491004559] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-7] [INFO] [1790782984.491122869] [rviz2]: OpenGl version: 4.6 (GLSL 4.6)
[rviz2-7] [INFO] [1790782984.598956100] [rviz2]: Stereo is NOT SUPPORTED
[gz-2] [1;33m[GUI] [Wrn] [Application.cc:908] [0m[1;33m[QT] file::/WorldStats/WorldStats.qml:53:3: QML RowLayout: Binding loop detected for property "x"[0m[1;33m[0m
[parameter_bridge-4] [WARN] [1790782984.682129437] [ros_gz_bridge]: New subscription discovered on topic '/scan', requesting incompatible QoS. No messages will be sent to it. Last incompatible policy: RELIABILITY_QOS_POLICY
[parameter_bridge-4] [WARN] [1790782984.692713008] [ros_gz_bridge]: New subscription discovered on topic '/camera/image_raw', requesting incompatible QoS. No messages will be sent to it. Last incompatible policy: RELIABILITY_QOS_POLICY
[rviz2-7] [INFO] [1790782984.914005347] [rviz2]: Stereo is NOT SUPPORTED
[gz-1] [1;33mWarning [Utils.cc:132][0m [/sdf/model[@name="vacuum"]/link[@name="camera_link"]/sensor[@name="camera"]/gz_frame_id:<urdf-string>:L0]: XML Element[gz_frame_id], child of element[sensor], not defined in SDF. Copying[gz_frame_id] as children of [sensor].
[gz-1] [1;33mWarning [Utils.cc:132][0m [/sdf/model[@name="vacuum"]/link[@name="lidar_link"]/sensor[@name="lidar"]/gz_frame_id:<urdf-string>:L0]: XML Element[gz_frame_id], child of element[sensor], not defined in SDF. Copying[gz_frame_id] as children of [sensor].
[gz-1] [INFO] [1790782985.094789078] [gz_ros_control]: [gz_ros2_control] Fixed joint ['camera_joint'] (Entity='53') is skipped.
[gz-1] [INFO] [1790782985.095322901] [gz_ros_control]: [gz_ros2_control] Fixed joint ['caster_joint'] (Entity='54') is skipped.
[gz-1] [INFO] [1790782985.095357484] [gz_ros_control]: [gz_ros2_control] Fixed joint ['lidar_joint'] (Entity='56') is skipped.
[gz-1] [INFO] [1790782985.096229565] [gz_ros_control]: Loading controller_manager
[gz-1] [INFO] [1790782985.119446169] [controller_manager]: Using ROS clock for triggering controller manager cycles.
[gz-1] [WARN] [1790782985.119532044] [controller_manager]: The resource manager is not yet initialized, will wait for the robot description to initialize it..
[gz-1] [INFO] [1790782985.136942218] [controller_manager]: Subscribing to '/robot_description' topic for robot description.
[gz-1] [WARN] [1790782985.137340064] [gz_ros_control]: Waiting RM to load and initialize hardware...
[gz-2] D3D12: Removing Device.
[gz-2] libEGL warning: egl: failed to create dri2 screen
[gz-1] [INFO] [1790782985.584191323] [controller_manager]: Received robot description from topic.
[gz-1] [INFO] [1790782985.584336545] [controller_manager]: Enforcing command limits is disabled. Command limits from URDF will be ignored.
[gz-1] [INFO] [1790782985.590149229] [gz_ros_control]: The position_proportional_gain has been set to: 0.1
[gz-1] [INFO] [1790782985.590317553] [gz_ros_control]: Loading joint: left_wheel_joint
[gz-1] [INFO] [1790782985.590332869] [gz_ros_control]: 	State:
[gz-1] [INFO] [1790782985.590340725] [gz_ros_control]: 		 position
[gz-1] [INFO] [1790782985.590345714] [gz_ros_control]: 		 velocity
[gz-1] [INFO] [1790782985.590354132] [gz_ros_control]: 	Command:
[gz-1] [INFO] [1790782985.590357440] [gz_ros_control]: 		 velocity
[gz-1] [INFO] [1790782985.590371838] [gz_ros_control]: Loading joint: right_wheel_joint
[gz-1] [INFO] [1790782985.590375596] [gz_ros_control]: 	State:
[gz-1] [INFO] [1790782985.590379485] [gz_ros_control]: 		 position
[gz-1] [INFO] [1790782985.590383372] [gz_ros_control]: 		 velocity
[gz-1] [INFO] [1790782985.590386900] [gz_ros_control]: 	Command:
[gz-1] [INFO] [1790782985.590390083] [gz_ros_control]: 		 velocity
[gz-1] [INFO] [1790782985.590558333] [controller_manager]: Initialize hardware 'VacuumSimulation' 
[gz-1] [WARN] [1790782985.590578958] [controller_manager.hardware_component.system.VacuumSimulation]: Executor is not available during hardware component initialization for 'VacuumSimulation'. Skipping node creation!
[gz-1] [INFO] [1790782985.590646177] [controller_manager]: Successful initialization of hardware 'VacuumSimulation'
[gz-1] [INFO] [1790782985.590811816] [controller_manager]: Activating component 'VacuumSimulation'.
[gz-1] [INFO] [1790782985.590848789] [resource_manager]: 'configure' hardware 'VacuumSimulation' 
[gz-1] [INFO] [1790782985.590857217] [gz_ros_control]: System Successfully configured!
[gz-1] [INFO] [1790782985.590865709] [resource_manager]: Successful 'configure' of hardware 'VacuumSimulation'
[gz-1] [INFO] [1790782985.590872973] [resource_manager]: 'activate' hardware 'VacuumSimulation' 
[gz-1] [INFO] [1790782985.590894085] [resource_manager]: Successful 'activate' of hardware 'VacuumSimulation'
[gz-1] [WARN] [1790782985.591053846] [controller_manager]: Component 'VacuumSimulation' does not have read or write statistics initialized, skipping registration.
[gz-1] [INFO] [1790782985.591069671] [controller_manager]: Resource Manager has been successfully initialized. Starting Controller Manager services...
[gz-1] [INFO] [1790782985.793783594] [controller_manager]: Loading controller : 'joint_state_broadcaster' of type 'joint_state_broadcaster/JointStateBroadcaster'
[gz-1] [INFO] [1790782985.794041168] [controller_manager]: Loading controller 'joint_state_broadcaster'
[gz-1] [WARN] [1790782985.804312082] [controller_manager]: The use of remapping arguments to the controller_manager node is deprecated. Please use the '--controller-ros-args' argument of the spawner to pass remapping arguments to the controller node.
[gz-1] [INFO] [1790782985.804586754] [controller_manager]: Controller 'joint_state_broadcaster' node arguments: --ros-args --params-file /home/robot/vacuum_ws/install/vacuum_sim/share/vacuum_sim/config/controllers.yaml --ros-args --remap /diff_drive_controller/odom:=/odom -p use_sim_time:=true --param use_sim_time:=true 
[spawner-8] [INFO] [1790782985.865965066] [spawner_joint_state_broadcaster]: Loaded joint_state_broadcaster
[gz-1] [INFO] [1790782985.872173653] [controller_manager]: Configuring controller: 'joint_state_broadcaster'
[gz-1] [INFO] [1790782985.872783474] [joint_state_broadcaster]: 'joints' or 'interfaces' parameter is empty. All available state interfaces will be published
[gz-1] [INFO] [1790782985.908317099] [controller_manager]: Activating controllers: [ joint_state_broadcaster ]
[gz-1] [WARN] [1790782987.248400416] [gz_ros_control]:  Desired controller update period (0.02 s) is slower than the gazebo simulation period (0.002 s).
[gz-2] [1;33mWarning [Utils.cc:132][0m [/sdf/model[@name="vacuum"]/link[@name="camera_link"]/sensor[@name="camera"]/gz_frame_id:<data-string>:L134]: XML Element[gz_frame_id], child of element[sensor], not defined in SDF. Copying[gz_frame_id] as children of [sensor].
[gz-2] [1;33mWarning [Utils.cc:132][0m [/sdf/model[@name="vacuum"]/link[@name="lidar_link"]/sensor[@name="lidar"]/gz_frame_id:<data-string>:L370]: XML Element[gz_frame_id], child of element[sensor], not defined in SDF. Copying[gz_frame_id] as children of [sensor].
[gz-1] [1;33m[Wrn] [Ogre2Camera.cc:423] [0m[1;33mOgre2Camera::SetVisibilityMask: Mask bits [0m[1;33mc0000000[0m[1;33m are set but will be ignored as they conflict with the [0m[1;33mreserved bits used internally by the ogre2 backend.[0m[1;33m[0m
[gz-1] [INFO] [1790782988.895295214] [controller_manager]: Successfully switched controllers!
[spawner-8] [INFO] [1790782988.918434447] [spawner_joint_state_broadcaster]: Configured and activated joint_state_broadcaster
[gz-1] [INFO] [1790782988.925598307] [controller_manager]: Loading controller : 'diff_drive_controller' of type 'diff_drive_controller/DiffDriveController'
[gz-1] [INFO] [1790782988.925707858] [controller_manager]: Loading controller 'diff_drive_controller'
[gz-1] [WARN] [1790782988.942710997] [controller_manager]: The use of remapping arguments to the controller_manager node is deprecated. Please use the '--controller-ros-args' argument of the spawner to pass remapping arguments to the controller node.
[gz-1] [INFO] [1790782988.944736864] [controller_manager]: Controller 'diff_drive_controller' node arguments: --ros-args --params-file /home/robot/vacuum_ws/install/vacuum_sim/share/vacuum_sim/config/controllers.yaml --ros-args --remap /diff_drive_controller/odom:=/odom -p use_sim_time:=true --param use_sim_time:=true 
[spawner-8] [INFO] [1790782989.021896959] [spawner_joint_state_broadcaster]: Loaded diff_drive_controller
[gz-1] [INFO] [1790782989.024474769] [controller_manager]: Configuring controller: 'diff_drive_controller'
[gz-1] [INFO] [1790782989.065117147] [controller_manager]: Activating controllers: [ diff_drive_controller ]
[gz-1] [INFO] [1790782989.082121800] [controller_manager]: Successfully switched controllers!
[spawner-8] [INFO] [1790782989.110715811] [spawner_joint_state_broadcaster]: Configured and activated diff_drive_controller
[INFO] [spawner-8]: process has finished cleanly [pid 1408]
[gz-1] [WARN] [1790782989.954734522] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790782990.992193288] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790782992.020549720] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790782993.122396702] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790782994.289496672] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790782995.386962906] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790782996.532160730] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790782997.594415644] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790782998.655015133] [diff_drive_controller]: Velocity command timed out. Braking.
[rviz2-7] [INFO] [1790782999.811644486] [rviz]: Message Filter dropping message: frame 'lidar_link' at time 0.004 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[gz-1] [WARN] [1790782999.859765968] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783000.979602151] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783002.117928912] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783003.269866260] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783004.337798590] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783005.396495756] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783004.818866015] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783005.871525039] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783006.912245480] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783008.056467172] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783009.094662667] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783010.134540609] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783011.146460541] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783012.194497462] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783013.229034748] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783014.259073965] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783015.270124391] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783016.293343933] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783021.150690143] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783022.191698728] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783023.254807725] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783024.567808745] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783025.582757843] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783026.663346638] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783027.687723478] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783028.701814816] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783029.717499238] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783030.725080015] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783032.211829187] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783033.366264871] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783034.505826611] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783035.671122390] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783035.073521787] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783036.191849751] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783037.230474279] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783038.268198964] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783039.307389335] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783040.345931385] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783041.367285597] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783042.375058314] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783043.382883202] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783044.441164712] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783045.476196300] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783046.505501536] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783047.540509763] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783048.562011183] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783049.571246141] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783050.585639209] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783051.600364691] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783052.622255326] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783053.743585761] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783054.826434184] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783055.831652809] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783056.916528528] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783057.945865778] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783058.955865191] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783059.979342235] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783060.991293749] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783062.021043668] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783063.026533553] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783064.078206071] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783065.086972591] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783066.097915041] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783065.474063515] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783066.588632484] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783067.604223507] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783068.610183240] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783069.687564602] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783070.716769259] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783071.733179434] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783072.740093447] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783073.770764914] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783074.785632872] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783075.799962660] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783076.836606671] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783077.871587717] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783078.883352363] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783079.883145399] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783080.889282163] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783081.902550465] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783082.926258975] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783084.200026427] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783085.497224186] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783086.643816093] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783087.795751753] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783088.877847116] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783090.054270405] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783091.239777086] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783092.732858411] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783094.060286532] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783095.551526227] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783096.661440170] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783097.771828578] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783097.167848065] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783098.183331619] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783099.231807514] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783100.282023719] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783101.307714071] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783102.347386357] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783103.358971327] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783104.385159275] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783105.406687210] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783106.440159656] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783107.460418714] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783108.495314729] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783109.508190648] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783110.515304958] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783111.530669523] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783112.539646554] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783113.648932976] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783114.708846457] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783115.717639505] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783116.730321433] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783117.813902518] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783118.824246321] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783119.838153782] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783120.857592185] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783121.875757060] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783122.905023715] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783123.954843510] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783124.974980577] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783125.991305269] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783127.008593384] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783128.038899854] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783127.477972400] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783128.499389084] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783129.520771667] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783130.534124318] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783131.544277283] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783132.558989735] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783133.566506052] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783134.574571157] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783135.594614370] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783136.602033129] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783137.638642890] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783138.646572626] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783139.664235410] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783140.698045910] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783141.712974450] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783142.721923208] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783143.857784502] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783144.922547045] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783145.933463694] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783146.974828476] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783148.015551324] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783149.037447809] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783150.045341390] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783151.251308773] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783152.380232124] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783153.473435363] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783154.781291117] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783156.011477784] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783157.181079722] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783158.237712112] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783159.296059800] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783158.803730988] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783159.829453572] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783160.840985526] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783161.843394308] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783162.902399107] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783163.926213763] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783164.958632777] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783165.976295840] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783167.001874952] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783168.059039393] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783169.064700267] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783170.067433097] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783171.117996165] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783172.159633572] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1790783173.454018593] [diff_drive_controller]: Velocity command timed out. Braking.
[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[INFO] [rviz2-7]: sending signal 'SIGINT' to process[rviz2-7]
[INFO] [twist_adapter.py-6]: sending signal 'SIGINT' to process[twist_adapter.py-6]
[INFO] [parameter_bridge-4]: sending signal 'SIGINT' to process[parameter_bridge-4]
[INFO] [robot_state_publisher-3]: sending signal 'SIGINT' to process[robot_state_publisher-3]
[INFO] [gz-2]: sending signal 'SIGINT' to process[gz-2]
[INFO] [gz-1]: sending signal 'SIGINT' to process[gz-1]
[rviz2-7] [INFO] [1790783173.484601116] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[parameter_bridge-4] [INFO] [1790783173.499206591] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[robot_state_publisher-3] [INFO] [1790783173.499455435] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [parameter_bridge-4]: process has finished cleanly [pid 1290]
[INFO] [robot_state_publisher-3]: process has finished cleanly [pid 1289]
[INFO] [twist_adapter.py-6]: process has finished cleanly [pid 1292]
[INFO] [rviz2-7]: process has finished cleanly [pid 1293]
[INFO] [gz-2]: process has finished cleanly [pid 1288]
[ERROR] [gz-1]: process has died [pid 1287, exit code -11, cmd 'gz sim -r -s -v 2 /home/robot/vacuum_ws/install/vacuum_sim/share/vacuum_sim/worlds/room.sdf'].


## validation/modern-drive-20261007

## validation/modern-drive-20261007/results.json

{
  "date": "2026-10-07",
  "scope": "simulator only",
  "tests": {
    "camera": {
      "target_fps": 60,
      "simulation_fps": 62.56311305242787,
      "wall_fps": 60.779299121060774,
      "frames": 180
    },
    "forward": {
      "signed_displacement_m": 2.4259256627277037,
      "peak_odometry_m_s": 1.7333333325829166,
      "first_10_percent_wall_s": 0.1339447560003464,
      "time_to_90_percent_wall_s": 0.33980555700009063,
      "neutral_stop_wall_s": 0.3714044120001745
    },
    "reverse": {
      "signed_displacement_m": -2.321481239286263,
      "peak_odometry_m_s": -1.0399999992263087,
      "first_10_percent_wall_s": 0.14133213600007366,
      "time_to_90_percent_wall_s": 0.256096781999986,
      "neutral_stop_wall_s": 0.2586458340001627
    },
    "neutral_stop_without_hold_button": true,
    "disarmed_stop": true,
    "steering": {
      "peak_rad_s": 2.6666666636267404,
      "time_to_90_percent_wall_s": 0.41659782800024914
    },
    "input_timeout_stop": true
  },
  "passed": true
}


## validation/furnished-20261007

## validation/furnished-20261007/isolated-guard.yaml

/furnished_guard_test/collision_monitor:
  ros__parameters:
    FootprintApproach:
      action_type: approach
      enabled: true
      footprint_topic: /local_costmap/published_footprint
      min_points: 1
      points: '[[0.140823, 0.0], [0.13754, 0.033326], [0.127819, 0.065371], [0.112034,
        0.094904], [0.09079, 0.12079], [0.064904, 0.142034], [0.035371, 0.157819],
        [0.003326, 0.16754], [-0.03, 0.170823], [-0.063326, 0.16754], [-0.095371,
        0.157819], [-0.124904, 0.142034], [-0.15079, 0.12079], [-0.172034, 0.094904],
        [-0.187819, 0.065371], [-0.19754, 0.033326], [-0.200823, 0.0], [-0.19754,
        -0.033326], [-0.187819, -0.065371], [-0.172034, -0.094904], [-0.15079, -0.12079],
        [-0.124904, -0.142034], [-0.095371, -0.157819], [-0.063326, -0.16754], [-0.03,
        -0.170823], [0.003326, -0.16754], [0.035371, -0.157819], [0.064904, -0.142034],
        [0.09079, -0.12079], [0.112034, -0.094904], [0.127819, -0.065371], [0.13754,
        -0.033326]]'
      simulation_time_step: 0.02
      time_before_collision: 0.55
      type: polygon
      visualize: false
    SlowZone:
      action_type: slowdown
      enabled: true
      forward:
        linear_max: 2.0
        linear_min: 0.001
        points: '[[-0.03, 0.25], [-0.03, -0.25], [1.7, -0.25], [1.7, 0.25]]'
        theta_max: 3.0
        theta_min: -3.0
      holonomic: false
      min_points: 1
      polygon_pub_topic: /furnished_guard_test/SlowZone
      reverse:
        linear_max: -0.001
        linear_min: -2.0
        points: '[[-1.2, 0.25], [-1.2, -0.25], [-0.03, -0.25], [-0.03, 0.25]]'
        theta_max: 3.0
        theta_min: -3.0
      rotation:
        linear_max: 2.0
        linear_min: -2.0
        points: '[[0.251355, 0.0], [0.245949, 0.05489], [0.229938, 0.10767], [0.203938,
          0.156312], [0.168948, 0.198948], [0.126312, 0.233938], [0.07767, 0.259938],
          [0.02489, 0.275949], [-0.03, 0.281355], [-0.08489, 0.275949], [-0.13767,
          0.259938], [-0.186312, 0.233938], [-0.228948, 0.198948], [-0.263938, 0.156312],
          [-0.289938, 0.10767], [-0.305949, 0.05489], [-0.311355, 0.0], [-0.305949,
          -0.05489], [-0.289938, -0.10767], [-0.263938, -0.156312], [-0.228948, -0.198948],
          [-0.186312, -0.233938], [-0.13767, -0.259938], [-0.08489, -0.275949], [-0.03,
          -0.281355], [0.02489, -0.275949], [0.07767, -0.259938], [0.126312, -0.233938],
          [0.168948, -0.198948], [0.203938, -0.156312], [0.229938, -0.10767], [0.245949,
          -0.05489]]'
        theta_max: 3.0
        theta_min: -3.0
      slowdown_ratio: 0.4
      type: velocity_polygon
      velocity_polygons:
      - forward
      - reverse
      - rotation
      visualize: true
    StopZone:
      action_type: stop
      enabled: true
      forward:
        linear_max: 2.0
        linear_min: 0.001
        points: '[[-0.03, 0.2], [-0.03, -0.2], [0.62, -0.2], [0.62, 0.2]]'
        theta_max: 3.0
        theta_min: -3.0
      holonomic: false
      min_points: 1
      polygon_pub_topic: /furnished_guard_test/StopZone
      reverse:
        linear_max: -0.001
        linear_min: -2.0
        points: '[[-0.6, 0.2], [-0.6, -0.2], [-0.03, -0.2], [-0.03, 0.2]]'
        theta_max: 3.0
        theta_min: -3.0
      rotation:
        linear_max: 2.0
        linear_min: -2.0
        points: '[[0.170968, 0.0], [0.167106, 0.039207], [0.15567, 0.076907], [0.137099,
          0.111652], [0.112106, 0.142106], [0.081652, 0.167099], [0.046907, 0.18567],
          [0.009207, 0.197106], [-0.03, 0.200968], [-0.069207, 0.197106], [-0.106907,
          0.18567], [-0.141652, 0.167099], [-0.172106, 0.142106], [-0.197099, 0.111652],
          [-0.21567, 0.076907], [-0.227106, 0.039207], [-0.230968, 0.0], [-0.227106,
          -0.039207], [-0.21567, -0.076907], [-0.197099, -0.111652], [-0.172106, -0.142106],
          [-0.141652, -0.167099], [-0.106907, -0.18567], [-0.069207, -0.197106], [-0.03,
          -0.200968], [0.009207, -0.197106], [0.046907, -0.18567], [0.081652, -0.167099],
          [0.112106, -0.142106], [0.137099, -0.111652], [0.15567, -0.076907], [0.167106,
          -0.039207]]'
        theta_max: 3.0
        theta_min: -3.0
      type: velocity_polygon
      velocity_polygons:
      - forward
      - reverse
      - rotation
      visualize: true
    base_frame_id: base_footprint
    base_shift_correction: true
    cmd_vel_in_topic: /furnished_guard_test/input
    cmd_vel_out_topic: /furnished_guard_test/output
    enable_stamped_cmd_vel: false
    observation_sources:
    - scan
    odom_frame_id: odom
    polygons:
    - StopZone
    - SlowZone
    - FootprintApproach
    scan:
      enabled: true
      max_height: 2.0
      min_height: 0.0
      source_timeout: 0.5
      topic: /furnished_guard_test/scan
      type: scan
    source_timeout: 0.5
    state_topic: /furnished_guard_test/state
    stop_pub_timeout: 2.0
    transform_tolerance: 0.2
    use_sim_time: true


## validation/furnished-20261007/preview-camera.sdf

<sdf version="1.9"><model name="robot_preview"><static>true</static>
<pose>.4 -.42 .19 0 .17 2.332</pose><link name="camera">
<sensor name="overview" type="camera"><topic>/robot_preview</topic><always_on>true</always_on><update_rate>1</update_rate>
<camera><horizontal_fov>1.0</horizontal_fov><image><width>1400</width><height>850</height><format>R8G8B8</format></image>
<clip><near>0.05</near><far>45</far></clip></camera></sensor></link></model></sdf>

## validation/furnished-20261007/isolated-guard.log

[INFO] [1791388513.144855075] [furnished_guard_test.collision_monitor]: 
	collision_monitor lifecycle node launched. 
	Waiting on external lifecycle transitions to activate
	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [1791388513.309692044] [furnished_guard_test.collision_monitor]: Configuring
[INFO] [1791388513.317791062] [collision_monitor]: [scan]: Creating Scan
[INFO] [1791388513.321792849] [collision_monitor]: [StopZone]: Creating Polygon
[INFO] [1791388513.321845397] [collision_monitor]: [StopZone]: Creating VelocityPolygon
[INFO] [1791388513.323431622] [collision_monitor]: [SlowZone]: Creating Polygon
[INFO] [1791388513.323477794] [collision_monitor]: [SlowZone]: Creating VelocityPolygon
[INFO] [1791388513.324571513] [collision_monitor]: [FootprintApproach]: Creating Polygon
[INFO] [1791388513.340908799] [furnished_guard_test.collision_monitor]: Activating
[INFO] [1791388513.341071715] [furnished_guard_test.collision_monitor]: Creating bond (collision_monitor) to lifecycle manager.
[WARN] [1791388513.344563988] [furnished_guard_test.collision_monitor]: Robot to stop due to invalid source. Either due to data not published yet, or to lack of new data received within the sensor timeout, or if impossible to transform data to base frame
[INFO] [1791388513.395154296] [furnished_guard_test.collision_monitor]: Robot to continue normal operation
[INFO] [1791388514.757982808] [furnished_guard_test.collision_monitor]: Robot to slowdown for 40.000000 percents due to SlowZone polygon
[INFO] [1791388516.129413205] [furnished_guard_test.collision_monitor]: Robot to stop due to StopZone polygon
[INFO] [1791388517.592206125] [furnished_guard_test.collision_monitor]: Robot to continue normal operation
[INFO] [1791388519.250653225] [furnished_guard_test.collision_monitor]: Robot to stop due to StopZone polygon
[INFO] [1791388520.721339199] [furnished_guard_test.collision_monitor]: Robot to continue normal operation
[INFO] [1791388522.225767960] [furnished_guard_test.collision_monitor]: Robot to stop due to StopZone polygon
[INFO] [1791388523.595349740] [furnished_guard_test.collision_monitor]: Robot to continue normal operation
[WARN] [1791388525.484958408] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.505556 seconds. Ignoring the source.
[WARN] [1791388525.485046252] [furnished_guard_test.collision_monitor]: Robot to stop due to invalid source. Either due to data not published yet, or to lack of new data received within the sensor timeout, or if impossible to transform data to base frame
[WARN] [1791388525.539721031] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.561111 seconds. Ignoring the source.
[WARN] [1791388525.595996952] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.605555 seconds. Ignoring the source.
[WARN] [1791388525.656463716] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.655555 seconds. Ignoring the source.
[WARN] [1791388525.709516374] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.688889 seconds. Ignoring the source.
[WARN] [1791388525.762628178] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.738889 seconds. Ignoring the source.
[WARN] [1791388525.815145432] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.788889 seconds. Ignoring the source.
[WARN] [1791388525.870358806] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.833333 seconds. Ignoring the source.
[WARN] [1791388525.923731643] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.877778 seconds. Ignoring the source.
[WARN] [1791388525.975717241] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.927778 seconds. Ignoring the source.
[WARN] [1791388526.030361672] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.983333 seconds. Ignoring the source.
[WARN] [1791388526.085959778] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.038889 seconds. Ignoring the source.
[WARN] [1791388526.142488585] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.094444 seconds. Ignoring the source.
[WARN] [1791388526.198084221] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.150000 seconds. Ignoring the source.
[WARN] [1791388526.251264216] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.194444 seconds. Ignoring the source.
[WARN] [1791388526.302631710] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.238889 seconds. Ignoring the source.
[WARN] [1791388526.354273214] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.288889 seconds. Ignoring the source.
[WARN] [1791388526.409576710] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.344444 seconds. Ignoring the source.
[INFO] [1791388526.463315282] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [1791388526.463510148] [furnished_guard_test.collision_monitor]: Running Nav2 LifecycleNode rcl preshutdown (collision_monitor)
[INFO] [1791388526.463593324] [furnished_guard_test.collision_monitor]: Deactivating
[INFO] [1791388526.463616225] [furnished_guard_test.collision_monitor]: Destroying bond (collision_monitor) to lifecycle manager.
[INFO] [1791388526.473960690] [furnished_guard_test.collision_monitor]: Cleaning up
[INFO] [1791388526.474140177] [collision_monitor]: [StopZone]: Destroying VelocityPolygon
[INFO] [1791388526.474154250] [collision_monitor]: [StopZone]: Destroying Polygon
[INFO] [1791388526.474164096] [collision_monitor]: [SlowZone]: Destroying VelocityPolygon
[INFO] [1791388526.474198035] [collision_monitor]: [SlowZone]: Destroying Polygon
[INFO] [1791388526.474204880] [collision_monitor]: [FootprintApproach]: Destroying Polygon
[INFO] [1791388526.474209632] [collision_monitor]: [scan]: Destroying Scan
[INFO] [1791388526.477625822] [furnished_guard_test.collision_monitor]: Destroying bond (collision_monitor) to lifecycle manager.
[INFO] [1791388526.489659286] [furnished_guard_test.collision_monitor]: Destroying


## validation/furnished-20261007/room-overview.png

## validation/furnished-20261007/directional-guard.json

{
  "scope": "isolated test topics; no robot command output",
  "tests": {
    "clear_fast_forward": 1.5,
    "forward_slow_front": 0.6000000000000001,
    "forward_stop_front": 0.0,
    "reverse_away_from_front": -0.9,
    "reverse_stop_rear": 0.0,
    "forward_away_from_rear": 1.5,
    "padded_body_contact_stop": 0.0,
    "clear_before_timeout": 1.5,
    "stale_lidar_stop": 0.0
  },
  "passed": true
}


## validation/furnished-20261007/robot-hardware.png

## validation/furnished-20261007/preview-bridge.log

[INFO] [1791389318.808038893] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/robot_preview (gz.msgs.Image) -> /robot_preview (sensor_msgs/msg/Image)] (Lazy 0)
[INFO] [1791389326.514945781] [rclcpp]: signal_handler(SIGINT/SIGTERM)


## validation/navigation.log

[INFO] [launch]: All log files can be found below /home/robot/.ros/log/2026-09-30-22-21-23-720960-Justin-1008
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [controller_server-1]: process started with pid [1033]
[INFO] [smoother_server-2]: process started with pid [1034]
[INFO] [planner_server-3]: process started with pid [1035]
[INFO] [route_server-4]: process started with pid [1036]
[INFO] [behavior_server-5]: process started with pid [1037]
[INFO] [bt_navigator-6]: process started with pid [1038]
[INFO] [waypoint_follower-7]: process started with pid [1039]
[INFO] [velocity_smoother-8]: process started with pid [1040]
[INFO] [collision_monitor-9]: process started with pid [1041]
[INFO] [opennav_docking-10]: process started with pid [1042]
[INFO] [lifecycle_manager-11]: process started with pid [1045]
[smoother_server-2] [INFO] [1790778084.523929708] [smoother_server]: 
[smoother_server-2] 	smoother_server lifecycle node launched. 
[smoother_server-2] 	Waiting on external lifecycle transitions to activate
[smoother_server-2] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[smoother_server-2] [INFO] [1790778084.545970611] [smoother_server]: Creating smoother server
[velocity_smoother-8] [INFO] [1790778084.639096255] [velocity_smoother]: 
[velocity_smoother-8] 	velocity_smoother lifecycle node launched. 
[velocity_smoother-8] 	Waiting on external lifecycle transitions to activate
[velocity_smoother-8] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[controller_server-1] [INFO] [1790778084.749398541] [controller_server]: 
[controller_server-1] 	controller_server lifecycle node launched. 
[controller_server-1] 	Waiting on external lifecycle transitions to activate
[controller_server-1] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[route_server-4] [INFO] [1790778084.756628775] [route_server]: 
[route_server-4] 	route_server lifecycle node launched. 
[route_server-4] 	Waiting on external lifecycle transitions to activate
[route_server-4] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[controller_server-1] [INFO] [1790778084.758173097] [controller_server]: Creating controller server
[lifecycle_manager-11] [INFO] [1790778084.759171483] [lifecycle_manager_navigation]: Creating
[lifecycle_manager-11] [INFO] [1790778084.835572880] [lifecycle_manager_navigation]: [34m[1mCreating and initializing lifecycle service clients[0m[0m
[planner_server-3] [INFO] [1790778084.928139227] [planner_server]: 
[planner_server-3] 	planner_server lifecycle node launched. 
[planner_server-3] 	Waiting on external lifecycle transitions to activate
[planner_server-3] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[planner_server-3] [INFO] [1790778084.979072948] [planner_server]: Creating
[collision_monitor-9] [INFO] [1790778084.999636351] [collision_monitor]: 
[collision_monitor-9] 	collision_monitor lifecycle node launched. 
[collision_monitor-9] 	Waiting on external lifecycle transitions to activate
[collision_monitor-9] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[opennav_docking-10] [INFO] [1790778085.010908788] [docking_server]: 
[opennav_docking-10] 	docking_server lifecycle node launched. 
[opennav_docking-10] 	Waiting on external lifecycle transitions to activate
[opennav_docking-10] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[opennav_docking-10] [INFO] [1790778085.011140113] [docking_server]: Creating docking_server
[bt_navigator-6] [INFO] [1790778085.072345919] [bt_navigator]: 
[bt_navigator-6] 	bt_navigator lifecycle node launched. 
[bt_navigator-6] 	Waiting on external lifecycle transitions to activate
[bt_navigator-6] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[bt_navigator-6] [INFO] [1790778085.080231946] [bt_navigator]: Creating
[waypoint_follower-7] [INFO] [1790778085.113020350] [waypoint_follower]: 
[waypoint_follower-7] 	waypoint_follower lifecycle node launched. 
[waypoint_follower-7] 	Waiting on external lifecycle transitions to activate
[waypoint_follower-7] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[waypoint_follower-7] [INFO] [1790778085.121375206] [waypoint_follower]: Creating
[controller_server-1] [INFO] [1790778085.131386046] [local_costmap.local_costmap]: 
[controller_server-1] 	local_costmap lifecycle node launched. 
[controller_server-1] 	Waiting on external lifecycle transitions to activate
[controller_server-1] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[controller_server-1] [INFO] [1790778085.141569711] [local_costmap.local_costmap]: Creating Costmap
[behavior_server-5] [INFO] [1790778085.188329666] [behavior_server]: 
[behavior_server-5] 	behavior_server lifecycle node launched. 
[behavior_server-5] 	Waiting on external lifecycle transitions to activate
[behavior_server-5] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[planner_server-3] [INFO] [1790778085.210375803] [global_costmap.global_costmap]: 
[planner_server-3] 	global_costmap lifecycle node launched. 
[planner_server-3] 	Waiting on external lifecycle transitions to activate
[planner_server-3] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[planner_server-3] [INFO] [1790778085.213368945] [global_costmap.global_costmap]: Creating Costmap
[lifecycle_manager-11] [INFO] [1790778085.780720035] [lifecycle_manager_navigation]: [34m[1mStarting managed nodes bringup...[0m[0m
[lifecycle_manager-11] [INFO] [1790778085.780789831] [lifecycle_manager_navigation]: [34m[1mConfiguring controller_server[0m[0m
[controller_server-1] [INFO] [1790778085.782634625] [controller_server]: Configuring controller interface
[controller_server-1] [INFO] [1790778085.782685029] [controller_server]: getting progress checker plugins..
[controller_server-1] [INFO] [1790778085.783553652] [controller_server]: getting goal checker plugins..
[controller_server-1] [INFO] [1790778085.783733014] [controller_server]: Controller frequency set to 20.0000Hz
[controller_server-1] [INFO] [1790778085.783799748] [local_costmap.local_costmap]: Configuring
[controller_server-1] [INFO] [1790778085.831643120] [local_costmap.local_costmap]: Using plugin "voxel_layer"
[controller_server-1] [INFO] [1790778085.845258776] [local_costmap.local_costmap]: Subscribed to Topics: scan
[controller_server-1] [INFO] [1790778085.898104685] [local_costmap.local_costmap]: Initialized plugin "voxel_layer"
[controller_server-1] [INFO] [1790778085.898188448] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[controller_server-1] [INFO] [1790778085.898834130] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[controller_server-1] [INFO] [1790778085.994580914] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[controller_server-1] [INFO] [1790778085.998283184] [controller_server]: Controller Server has progress_checker  progress checkers available.
[controller_server-1] [INFO] [1790778086.006780779] [controller_server]: Created goal checker : general_goal_checker of type nav2_controller::SimpleGoalChecker
[controller_server-1] [INFO] [1790778086.009934907] [controller_server]: Controller Server has general_goal_checker  goal checkers available.
[controller_server-1] [INFO] [1790778086.024931817] [controller_server]: Created controller : FollowPath of type dwb_core::DWBLocalPlanner
[controller_server-1] [INFO] [1790778086.025745273] [controller_server]: Setting transform_tolerance to 0.200000
[controller_server-1] [INFO] [1790778086.079698771] [controller_server]: Using critic "RotateToGoal" (dwb_critics::RotateToGoalCritic)
[controller_server-1] [INFO] [1790778086.085765280] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1790778086.085994097] [controller_server]: Using critic "Oscillation" (dwb_critics::OscillationCritic)
[controller_server-1] [INFO] [1790778086.086220790] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1790778086.086309119] [controller_server]: Using critic "BaseObstacle" (dwb_critics::BaseObstacleCritic)
[controller_server-1] [INFO] [1790778086.086395226] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1790778086.086442749] [controller_server]: Using critic "GoalAlign" (dwb_critics::GoalAlignCritic)
[controller_server-1] [INFO] [1790778086.086814939] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1790778086.086903751] [controller_server]: Using critic "PathAlign" (dwb_critics::PathAlignCritic)
[controller_server-1] [INFO] [1790778086.092090488] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1790778086.093722850] [controller_server]: Using critic "PathDist" (dwb_critics::PathDistCritic)
[controller_server-1] [INFO] [1790778086.096219670] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1790778086.097907302] [controller_server]: Using critic "GoalDist" (dwb_critics::GoalDistCritic)
[controller_server-1] [INFO] [1790778086.106454822] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1790778086.106546300] [controller_server]: Controller Server has FollowPath  controllers available.
[lifecycle_manager-11] [INFO] [1790778086.169193445] [lifecycle_manager_navigation]: [34m[1mConfiguring smoother_server[0m[0m
[smoother_server-2] [INFO] [1790778086.169868468] [smoother_server]: Configuring smoother server
[smoother_server-2] [INFO] [1790778086.235724987] [smoother_server]: Created smoother : simple_smoother of type nav2_smoother::SimpleSmoother
[smoother_server-2] [INFO] [1790778086.236167154] [smoother_server]: Smoother Server has simple_smoother  smoothers available.
[lifecycle_manager-11] [INFO] [1790778086.286508374] [lifecycle_manager_navigation]: [34m[1mConfiguring planner_server[0m[0m
[planner_server-3] [INFO] [1790778086.287309407] [planner_server]: Configuring
[planner_server-3] [INFO] [1790778086.287361057] [global_costmap.global_costmap]: Configuring
[planner_server-3] [INFO] [1790778086.334865919] [global_costmap.global_costmap]: Using plugin "static_layer"
[planner_server-3] [INFO] [1790778086.343323274] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[planner_server-3] [INFO] [1790778086.350239429] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[planner_server-3] [INFO] [1790778086.350309648] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[planner_server-3] [INFO] [1790778086.350714512] [global_costmap.global_costmap]: Subscribed to Topics: scan
[planner_server-3] [INFO] [1790778086.395350547] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[planner_server-3] [INFO] [1790778086.395551110] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[planner_server-3] [INFO] [1790778086.403286172] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[planner_server-3] [INFO] [1790778086.712142679] [planner_server]: Created global planner plugin GridBased of type nav2_navfn_planner::NavfnPlanner
[planner_server-3] [INFO] [1790778086.714259334] [planner_server]: Configuring plugin GridBased of type NavfnPlanner
[planner_server-3] [INFO] [1790778086.730601696] [planner_server]: Planner Server has GridBased  planners available.
[lifecycle_manager-11] [INFO] [1790778086.815434276] [lifecycle_manager_navigation]: [34m[1mConfiguring route_server[0m[0m
[route_server-4] [INFO] [1790778086.819623363] [route_server]: Configuring
[route_server-4] [INFO] [1790778087.015611556] [route_server]: Created GraphFileLoader GeoJsonGraphFileLoader of type nav2_route::GeoJsonGraphFileLoader
[route_server-4] [INFO] [1790778087.015845478] [route_server]: Configuring geojson graph file loader
[route_server-4] [INFO] [1790778087.015861997] [route_server]: No graph file provided to load yet.
[route_server-4] [INFO] [1790778087.031556425] [route_server]: Created edge cost function plugin DistanceScorer of type nav2_route::DistanceScorer
[route_server-4] [INFO] [1790778087.031641840] [route_server]: Configuring distance scorer.
[route_server-4] [INFO] [1790778087.039318841] [route_server]: Created edge cost function plugin CostmapScorer of type nav2_route::CostmapScorer
[route_server-4] [INFO] [1790778087.039385057] [route_server]: Configuring costmap scorer.
[route_server-4] [INFO] [1790778087.060104700] [route_server]: Created route operation AdjustSpeedLimit of type nav2_route::AdjustSpeedLimit
[route_server-4] [INFO] [1790778087.060207470] [route_server]: Configuring Adjust speed limit operation.
[route_server-4] [INFO] [1790778087.071378404] [route_server]: Created route operation ReroutingService of type nav2_route::ReroutingService
[route_server-4] [INFO] [1790778087.071500848] [route_server]: Configuring Rerouting service operation.
[route_server-4] [INFO] [1790778087.085219935] [route_server]: Created route operation CollisionMonitor of type nav2_route::CollisionMonitor
[route_server-4] [INFO] [1790778087.085896169] [route_server]: Using costmap topic: local_costmap/costmap_raw instead of server costmap topic: global_costmap/costmap_raw for CollisionMonitor.
[lifecycle_manager-11] [INFO] [1790778087.101432239] [lifecycle_manager_navigation]: [34m[1mConfiguring behavior_server[0m[0m
[behavior_server-5] [INFO] [1790778087.104079386] [behavior_server]: Configuring
[behavior_server-5] [INFO] [1790778087.142443384] [behavior_server]: Creating behavior plugin spin of type nav2_behaviors::Spin
[behavior_server-5] [INFO] [1790778087.154594780] [behavior_server]: Creating behavior plugin backup of type nav2_behaviors::BackUp
[behavior_server-5] [INFO] [1790778087.160486204] [behavior_server]: Creating behavior plugin drive_on_heading of type nav2_behaviors::DriveOnHeading
[behavior_server-5] [INFO] [1790778087.169758993] [behavior_server]: Creating behavior plugin assisted_teleop of type nav2_behaviors::AssistedTeleop
[behavior_server-5] [INFO] [1790778087.188626546] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors::Wait
[behavior_server-5] [INFO] [1790778087.232660866] [behavior_server]: Configuring spin
[behavior_server-5] [INFO] [1790778087.295736155] [behavior_server]: Configuring backup
[planner_server-3] [INFO] [1790778087.311479599] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 119 X 119 at 0.050000 m/pix
[behavior_server-5] [INFO] [1790778087.335196257] [behavior_server]: Configuring drive_on_heading
[behavior_server-5] [INFO] [1790778087.379492045] [behavior_server]: Configuring assisted_teleop
[behavior_server-5] [INFO] [1790778087.426373655] [behavior_server]: Configuring wait
[lifecycle_manager-11] [INFO] [1790778087.473943981] [lifecycle_manager_navigation]: [34m[1mConfiguring velocity_smoother[0m[0m
[velocity_smoother-8] [INFO] [1790778087.476815210] [velocity_smoother]: Configuring velocity smoother
[lifecycle_manager-11] [INFO] [1790778087.510216474] [lifecycle_manager_navigation]: [34m[1mConfiguring collision_monitor[0m[0m
[collision_monitor-9] [INFO] [1790778087.511428930] [collision_monitor]: Configuring
[collision_monitor-9] [INFO] [1790778087.545517165] [collision_monitor]: [scan]: Creating Scan
[collision_monitor-9] [INFO] [1790778087.558659421] [collision_monitor]: [FootprintApproach]: Creating Polygon
[collision_monitor-9] [INFO] [1790778087.560928052] [collision_monitor]: [FootprintApproach]: Polygon points are not defined. Using dynamic subscription instead.
[collision_monitor-9] [INFO] [1790778087.565673852] [collision_monitor]: [FootprintApproach]: Making footprint subscriber on /local_costmap/published_footprint topic
[lifecycle_manager-11] [INFO] [1790778087.631871283] [lifecycle_manager_navigation]: [34m[1mConfiguring bt_navigator[0m[0m
[bt_navigator-6] [INFO] [1790778087.634933247] [bt_navigator]: Configuring
[bt_navigator-6] [INFO] [1790778087.682160311] [bt_navigator]: Creating navigator id navigate_to_pose of type nav2_bt_navigator::NavigateToPoseNavigator
[bt_navigator-6] [INFO] [1790778088.317125120] [bt_navigator]: Creating navigator id navigate_through_poses of type nav2_bt_navigator::NavigateThroughPosesNavigator
[lifecycle_manager-11] [INFO] [1790778088.487179359] [lifecycle_manager_navigation]: [34m[1mConfiguring waypoint_follower[0m[0m
[waypoint_follower-7] [INFO] [1790778088.488085229] [waypoint_follower]: Configuring
[waypoint_follower-7] [INFO] [1790778088.624499701] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[lifecycle_manager-11] [INFO] [1790778088.632061285] [lifecycle_manager_navigation]: [34m[1mConfiguring docking_server[0m[0m
[opennav_docking-10] [INFO] [1790778088.635593058] [docking_server]: Configuring docking_server
[opennav_docking-10] [INFO] [1790778088.635724851] [docking_server]: Controller frequency set to 50.0000Hz
[opennav_docking-10] [INFO] [1790778088.815316107] [docking_server]: Created charging dock plugin simple_charging_dock of type opennav_docking::SimpleChargingDock
[opennav_docking-10] [WARN] [1790778088.864144221] [docking_server]: Dock database filepath nor dock parameters set. Docking actions can only be executed specifying the dock pose via the action request. Or update the dock database via the reload_database service.
[opennav_docking-10] [INFO] [1790778088.864236373] [docking_server]: Docking Server has 1 dock types and 0 dock instances available.
[lifecycle_manager-11] [INFO] [1790778088.875288597] [lifecycle_manager_navigation]: [34m[1mActivating controller_server[0m[0m
[controller_server-1] [INFO] [1790778088.880754254] [controller_server]: Activating
[controller_server-1] [INFO] [1790778088.880844361] [local_costmap.local_costmap]: Activating
[controller_server-1] [INFO] [1790778088.880857770] [local_costmap.local_costmap]: Checking transform
[controller_server-1] [INFO] [1790778088.882453021] [local_costmap.local_costmap]: start
[controller_server-1] [INFO] [1790778089.094403469] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1790778089.229949570] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[lifecycle_manager-11] [INFO] [1790778089.230056473] [lifecycle_manager_navigation]: [34m[1mActivating smoother_server[0m[0m
[smoother_server-2] [INFO] [1790778089.231835488] [smoother_server]: Activating
[smoother_server-2] [INFO] [1790778089.231917954] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1790778089.362018737] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[lifecycle_manager-11] [INFO] [1790778089.362137149] [lifecycle_manager_navigation]: [34m[1mActivating planner_server[0m[0m
[planner_server-3] [INFO] [1790778089.363464744] [planner_server]: Activating
[planner_server-3] [INFO] [1790778089.363510093] [global_costmap.global_costmap]: Activating
[planner_server-3] [INFO] [1790778089.363518322] [global_costmap.global_costmap]: Checking transform
[planner_server-3] [INFO] [1790778089.363760974] [global_costmap.global_costmap]: start
[planner_server-3] [INFO] [1790778090.366535999] [planner_server]: Activating plugin GridBased of type NavfnPlanner
[planner_server-3] [INFO] [1790778090.375663611] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1790778090.505106068] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[lifecycle_manager-11] [INFO] [1790778090.505329460] [lifecycle_manager_navigation]: [34m[1mActivating route_server[0m[0m
[route_server-4] [INFO] [1790778090.506979087] [route_server]: Activating
[route_server-4] [INFO] [1790778090.507384967] [route_server]: Creating bond (route_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1790778090.643097621] [lifecycle_manager_navigation]: Server route_server connected with bond.
[lifecycle_manager-11] [INFO] [1790778090.643187822] [lifecycle_manager_navigation]: [34m[1mActivating behavior_server[0m[0m
[behavior_server-5] [INFO] [1790778090.647106298] [behavior_server]: Activating
[behavior_server-5] [INFO] [1790778090.647480187] [behavior_server]: Activating spin
[behavior_server-5] [INFO] [1790778090.647510220] [behavior_server]: Activating backup
[behavior_server-5] [INFO] [1790778090.647523297] [behavior_server]: Activating drive_on_heading
[behavior_server-5] [INFO] [1790778090.647535671] [behavior_server]: Activating assisted_teleop
[behavior_server-5] [INFO] [1790778090.647567573] [behavior_server]: Activating wait
[behavior_server-5] [INFO] [1790778090.647592359] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1790778090.773049859] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[lifecycle_manager-11] [INFO] [1790778090.773133886] [lifecycle_manager_navigation]: [34m[1mActivating velocity_smoother[0m[0m
[velocity_smoother-8] [INFO] [1790778090.774148443] [velocity_smoother]: Activating
[velocity_smoother-8] [INFO] [1790778090.774272585] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1790778090.907869457] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[lifecycle_manager-11] [INFO] [1790778090.907982760] [lifecycle_manager_navigation]: [34m[1mActivating collision_monitor[0m[0m
[collision_monitor-9] [INFO] [1790778090.909756140] [collision_monitor]: Activating
[collision_monitor-9] [INFO] [1790778090.909832781] [collision_monitor]: Creating bond (collision_monitor) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1790778091.020663938] [lifecycle_manager_navigation]: Server collision_monitor connected with bond.
[lifecycle_manager-11] [INFO] [1790778091.020752676] [lifecycle_manager_navigation]: [34m[1mActivating bt_navigator[0m[0m
[bt_navigator-6] [INFO] [1790778091.022355617] [bt_navigator]: Activating
[bt_navigator-6] [INFO] [1790778091.604504519] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1790778091.733054125] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[lifecycle_manager-11] [INFO] [1790778091.733126856] [lifecycle_manager_navigation]: [34m[1mActivating waypoint_follower[0m[0m
[waypoint_follower-7] [INFO] [1790778091.734941130] [waypoint_follower]: Activating
[waypoint_follower-7] [INFO] [1790778091.735057838] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1790778091.873935180] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[lifecycle_manager-11] [INFO] [1790778091.874046854] [lifecycle_manager_navigation]: [34m[1mActivating docking_server[0m[0m
[opennav_docking-10] [INFO] [1790778091.887127941] [docking_server]: Activating docking_server
[opennav_docking-10] [INFO] [1790778091.973606820] [docking_server]: Creating bond (docking_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1790778092.107210370] [lifecycle_manager_navigation]: Server docking_server connected with bond.
[lifecycle_manager-11] [INFO] [1790778092.107278773] [lifecycle_manager_navigation]: [34m[1mManaged nodes are active[0m[0m
[lifecycle_manager-11] [INFO] [1790778092.107293426] [lifecycle_manager_navigation]: [34m[1mCreating bond timer...[0m[0m
[planner_server-3] [INFO] [1790778091.914294940] [global_costmap.global_costmap]: Message Filter dropping message: frame 'lidar_link' at time 1119.400 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[bt_navigator-6] [INFO] [1790778106.930502632] [bt_navigator]: Begin navigating from current location (0.57, -0.00) to (1.00, 0.00)
[controller_server-1] [INFO] [1790778106.968263311] [controller_server]: Received a goal, begin computing control effort.
[controller_server-1] [WARN] [1790778106.968683071] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded general_goal_checker . This warning will appear once.
[controller_server-1] [WARN] [1790778106.968750060] [controller_server]: No progress checker was specified in parameter 'current_progress_checker'. Server will use only plugin loaded progress_checker . This warning will appear once.
[controller_server-1] [INFO] [1790778108.069079933] [controller_server]: Passing new path to controller.
[controller_server-1] [WARN] [1790778108.885454386] [controller_server]: Control loop missed its desired rate of 20.0000 Hz. Current loop rate is inf Hz.
[controller_server-1] [INFO] [1790778109.085837932] [controller_server]: Passing new path to controller.
[controller_server-1] [INFO] [1790778110.142946300] [controller_server]: Passing new path to controller.
[controller_server-1] [INFO] [1790778110.785744892] [controller_server]: Reached the goal!
[bt_navigator-6] [INFO] [1790778110.821030197] [bt_navigator]: Goal succeeded
[planner_server-3] [INFO] [1790778111.957396209] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 119 X 119 at 0.050000 m/pix
[planner_server-3] [INFO] [1790778122.912052090] [global_costmap.global_costmap]: Message Filter dropping message: frame 'lidar_link' at time 1139.500 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[planner_server-3] [INFO] [1790778185.801100814] [global_costmap.global_costmap]: Message Filter dropping message: frame 'lidar_link' at time 1172.800 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[planner_server-3] [INFO] [1790778216.701122917] [global_costmap.global_costmap]: Message Filter dropping message: frame 'lidar_link' at time 1187.000 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[planner_server-3] [INFO] [1790778248.131368927] [global_costmap.global_costmap]: Message Filter dropping message: frame 'lidar_link' at time 1199.900 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[planner_server-3] [INFO] [1790778279.022484138] [global_costmap.global_costmap]: Message Filter dropping message: frame 'lidar_link' at time 1212.200 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[planner_server-3] [INFO] [1790778310.087398519] [global_costmap.global_costmap]: Message Filter dropping message: frame 'lidar_link' at time 1226.400 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[controller_server-1] [INFO] [1790778332.247083762] [local_costmap.local_costmap]: Message Filter dropping message: frame 'lidar_link' at time 1236.400 for reason 'the timestamp on the message is earlier than all the data in the transform cache'
[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[INFO] [lifecycle_manager-11]: sending signal 'SIGINT' to process[lifecycle_manager-11]
[INFO] [opennav_docking-10]: sending signal 'SIGINT' to process[opennav_docking-10]
[INFO] [collision_monitor-9]: sending signal 'SIGINT' to process[collision_monitor-9]
[INFO] [velocity_smoother-8]: sending signal 'SIGINT' to process[velocity_smoother-8]
[INFO] [waypoint_follower-7]: sending signal 'SIGINT' to process[waypoint_follower-7]
[INFO] [bt_navigator-6]: sending signal 'SIGINT' to process[bt_navigator-6]
[INFO] [behavior_server-5]: sending signal 'SIGINT' to process[behavior_server-5]
[INFO] [route_server-4]: sending signal 'SIGINT' to process[route_server-4]
[INFO] [planner_server-3]: sending signal 'SIGINT' to process[planner_server-3]
[INFO] [smoother_server-2]: sending signal 'SIGINT' to process[smoother_server-2]
[INFO] [controller_server-1]: sending signal 'SIGINT' to process[controller_server-1]
[lifecycle_manager-11] [INFO] [1790778336.847727833] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-11] [INFO] [1790778336.848110238] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[lifecycle_manager-11] [INFO] [1790778336.848304516] [lifecycle_manager_navigation]: [34m[1mTerminating bond timer...[0m[0m
[opennav_docking-10] [INFO] [1790778336.848985754] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[opennav_docking-10] [INFO] [1790778336.849135435] [docking_server]: Running Nav2 LifecycleNode rcl preshutdown (docking_server)
[opennav_docking-10] [INFO] [1790778336.849274601] [docking_server]: Deactivating docking_server
[collision_monitor-9] [INFO] [1790778336.861497489] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[collision_monitor-9] [INFO] [1790778336.861877777] [collision_monitor]: Running Nav2 LifecycleNode rcl preshutdown (collision_monitor)
[collision_monitor-9] [INFO] [1790778336.861988507] [collision_monitor]: Deactivating
[collision_monitor-9] [INFO] [1790778336.862013098] [collision_monitor]: Destroying bond (collision_monitor) to lifecycle manager.
[velocity_smoother-8] [INFO] [1790778336.896217644] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[velocity_smoother-8] [INFO] [1790778336.896379091] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[velocity_smoother-8] [INFO] [1790778336.896484478] [velocity_smoother]: Deactivating
[velocity_smoother-8] [INFO] [1790778336.896512763] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[collision_monitor-9] [INFO] [1790778336.903069945] [collision_monitor]: Cleaning up
[collision_monitor-9] [INFO] [1790778336.903137739] [collision_monitor]: [FootprintApproach]: Destroying Polygon
[collision_monitor-9] [INFO] [1790778336.903155523] [collision_monitor]: [scan]: Destroying Scan
[waypoint_follower-7] [INFO] [1790778336.962783056] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[waypoint_follower-7] [INFO] [1790778336.962945669] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[waypoint_follower-7] [INFO] [1790778336.963057248] [waypoint_follower]: Deactivating
[waypoint_follower-7] [INFO] [1790778336.963083112] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[behavior_server-5] [INFO] [1790778336.967132715] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[behavior_server-5] [INFO] [1790778336.967284317] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[behavior_server-5] [INFO] [1790778336.971347915] [behavior_server]: Deactivating
[behavior_server-5] [INFO] [1790778336.971419950] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[bt_navigator-6] [INFO] [1790778336.967347030] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[bt_navigator-6] [INFO] [1790778336.967418465] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[bt_navigator-6] [INFO] [1790778336.967512037] [bt_navigator]: Deactivating
[bt_navigator-6] [INFO] [1790778336.967545583] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[velocity_smoother-8] [INFO] [1790778336.968599633] [velocity_smoother]: Cleaning up
[velocity_smoother-8] [INFO] [1790778336.968649557] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[collision_monitor-9] [INFO] [1790778336.971669496] [collision_monitor]: Destroying bond (collision_monitor) to lifecycle manager.
[velocity_smoother-8] [INFO] [1790778336.982131819] [velocity_smoother]: Destroying
[route_server-4] [INFO] [1790778336.998755434] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[route_server-4] [INFO] [1790778336.999000678] [route_server]: Running Nav2 LifecycleNode rcl preshutdown (route_server)
[route_server-4] [INFO] [1790778337.014813319] [route_server]: Deactivating
[controller_server-1] [INFO] [1790778337.054725035] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[controller_server-1] [INFO] [1790778337.054929800] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[controller_server-1] [INFO] [1790778337.055090421] [controller_server]: Deactivating
[controller_server-1] [INFO] [1790778337.055162740] [local_costmap.local_costmap]: Deactivating
[planner_server-3] [INFO] [1790778337.057892845] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[planner_server-3] [INFO] [1790778337.058114276] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[smoother_server-2] [INFO] [1790778337.058174946] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[smoother_server-2] [INFO] [1790778337.058284114] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[smoother_server-2] [INFO] [1790778337.058363764] [smoother_server]: Deactivating
[smoother_server-2] [INFO] [1790778337.058383008] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[planner_server-3] [INFO] [1790778337.060242561] [planner_server]: Deactivating
[planner_server-3] [INFO] [1790778337.060311363] [global_costmap.global_costmap]: Deactivating
[waypoint_follower-7] [INFO] [1790778337.064194381] [waypoint_follower]: Cleaning up
[route_server-4] [INFO] [1790778337.066769179] [route_server]: Destroying bond (route_server) to lifecycle manager.
[bt_navigator-6] [INFO] [1790778337.068346293] [bt_navigator]: Cleaning up
[behavior_server-5] [INFO] [1790778337.071868991] [behavior_server]: Cleaning up
[behavior_server-5] [INFO] [1790778337.077473294] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[opennav_docking-10] [INFO] [1790778337.086015306] [docking_server]: Destroying bond (docking_server) to lifecycle manager.
[controller_server-1] [INFO] [1790778337.119544281] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[collision_monitor-9] [INFO] [1790778337.160830901] [collision_monitor]: Destroying
[smoother_server-2] [INFO] [1790778337.165452553] [smoother_server]: Cleaning up
[route_server-4] [INFO] [1790778337.172395515] [route_server]: Cleaning up
[planner_server-3] [INFO] [1790778337.204446288] [planner_server]: Deactivating plugin GridBased of type NavfnPlanner
[planner_server-3] [INFO] [1790778337.204532100] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[waypoint_follower-7] [INFO] [1790778337.227734758] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[controller_server-1] [INFO] [1790778337.228536592] [controller_server]: Cleaning up
[controller_server-1] [INFO] [1790778337.228874668] [local_costmap.local_costmap]: Cleaning up
[opennav_docking-10] [INFO] [1790778337.232401077] [docking_server]: Cleaning up docking_server
[route_server-4] [INFO] [1790778337.307519332] [route_server]: Destroying bond (route_server) to lifecycle manager.
[route_server-4] [INFO] [1790778337.322998325] [route_server]: Destroying
[planner_server-3] [INFO] [1790778337.325247748] [planner_server]: Cleaning up
[waypoint_follower-7] [INFO] [1790778337.334753326] [waypoint_follower]: Destroying
[opennav_docking-10] [INFO] [1790778337.401283228] [docking_server]: Destroying bond (docking_server) to lifecycle manager.
[behavior_server-5] [INFO] [1790778337.406443317] [behavior_server]: Destroying
[smoother_server-2] [INFO] [1790778337.481570544] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[opennav_docking-10] [INFO] [1790778337.493237424] [docking_server]: Destroying
[smoother_server-2] [INFO] [1790778337.503220032] [smoother_server]: Destroying
[planner_server-3] [INFO] [1790778337.504582231] [global_costmap.global_costmap]: Cleaning up
[INFO] [velocity_smoother-8]: process has finished cleanly [pid 1040]
[planner_server-3] [INFO] [1790778337.606314267] [planner_server]: Cleaning up plugin GridBased of type NavfnPlanner
[planner_server-3] [INFO] [1790778337.607518390] [planner_server]: Destroying plugin GridBased of type NavfnPlanner
[INFO] [collision_monitor-9]: process has finished cleanly [pid 1041]
[INFO] [behavior_server-5]: process has finished cleanly [pid 1037]
[INFO] [waypoint_follower-7]: process has finished cleanly [pid 1039]
[INFO] [opennav_docking-10]: process has finished cleanly [pid 1042]
[controller_server-1] [INFO] [1790778337.783688756] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[planner_server-3] [INFO] [1790778337.817070185] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[controller_server-1] [INFO] [1790778337.840031967] [local_costmap.local_costmap]: Destroying
[planner_server-3] [INFO] [1790778337.851415460] [global_costmap.global_costmap]: Destroying
[INFO] [route_server-4]: process has finished cleanly [pid 1036]
[controller_server-1] [INFO] [1790778337.959804656] [controller_server]: Destroying
[INFO] [smoother_server-2]: process has finished cleanly [pid 1034]
[planner_server-3] [INFO] [1790778338.008687635] [planner_server]: Destroying
[lifecycle_manager-11] [INFO] [1790778338.112392763] [lifecycle_manager_navigation]: Destroying lifecycle_manager_navigation
[INFO] [controller_server-1]: process has finished cleanly [pid 1033]
[INFO] [lifecycle_manager-11]: process has finished cleanly [pid 1045]
[bt_navigator-6] [INFO] [1790778338.378235601] [bt_navigator]: Completed Cleaning up
[bt_navigator-6] [INFO] [1790778338.378356323] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[INFO] [planner_server-3]: process has finished cleanly [pid 1035]
[bt_navigator-6] [INFO] [1790778338.385218405] [bt_navigator]: Destroying
[INFO] [bt_navigator-6]: process has finished cleanly [pid 1038]


## validation/navigation.pid

## validation/direct-drive-20261007

## validation/direct-drive-20261007/results.json

{
  "date": "2026-10-07",
  "scope": "simulator only",
  "tests": {
    "camera": {
      "target_fps": 60,
      "simulation_fps": 62.44186670930361,
      "wall_fps": 61.68804157766852,
      "frames": 180
    },
    "forward": {
      "signed_displacement_m": 0.707061642259529,
      "peak_odometry_m_s": 0.5299999998527953
    },
    "reverse": {
      "signed_displacement_m": -0.7481480675912968,
      "peak_odometry_m_s": -0.33399999990568163
    },
    "released_stop": true,
    "input_timeout_stop": true
  },
  "passed": true
}


## validation/lab-20261007

## validation/lab-20261007/results.json

{
  "date": "2026-10-07",
  "scope": "simulator only",
  "tests": {
    "circular_robot_goal": {
      "status": 4,
      "error_code": 0
    },
    "map_save": true,
    "manual_hold_and_release": {
      "movement_m": 0.18666664767127053,
      "released_speed_m_s": -2.105212574635046e-14
    },
    "input_timeout_stop": true,
    "bridge_eof_cleanup": true
  },
  "passed": true
}


## validation/furnished-robot-camera.png

## validation/autonomy-20261006

## validation/autonomy-20261006/mapping.log

[INFO] [launch]: All log files can be found below /home/robot/.ros/log/2026-10-06-00-35-27-915042-Justin-622
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [async_slam_toolbox_node-1]: process started with pid [637]
[async_slam_toolbox_node-1] [INFO] [1791218128.551699373] [slam_toolbox]: Configuring
[async_slam_toolbox_node-1] [INFO] [1791218128.581914820] [slam_toolbox]: Using solver plugin solver_plugins::CeresSolver
[async_slam_toolbox_node-1] [INFO] [1791218128.582420874] [slam_toolbox]: CeresSolver: Using SCHUR_JACOBI preconditioner.
[INFO] [launch.user]: [LifecycleLaunch] Slamtoolbox node is activating.
[async_slam_toolbox_node-1] [INFO] [1791218128.632536578] [slam_toolbox]: Activating
[async_slam_toolbox_node-1] Registering sensor: [Custom Described Lidar]
[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[INFO] [async_slam_toolbox_node-1]: sending signal 'SIGINT' to process[async_slam_toolbox_node-1]
[INFO] [async_slam_toolbox_node-1]: process has finished cleanly [pid 637]
[async_slam_toolbox_node-1] [INFO] [1791218162.903563667] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[async_slam_toolbox_node-1] Unregistering sensor: Custom Described Lidar


## validation/autonomy-20261006/sim.log

[INFO] [launch]: All log files can be found below /home/robot/.ros/log/2026-10-06-00-35-18-998068-Justin-443
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [gz-1]: process started with pid [469]
[INFO] [robot_state_publisher-2]: process started with pid [470]
[INFO] [parameter_bridge-3]: process started with pid [471]
[INFO] [create-4]: process started with pid [472]
[INFO] [twist_adapter.py-5]: process started with pid [473]
[create-4] [INFO] [1791218119.374070161] [ros_gz_sim]: Waiting messages on topic [/robot_description].
[robot_state_publisher-2] [INFO] [1791218119.402749304] [robot_state_publisher]: Robot initialized
[create-4] [INFO] [1791218120.302904753] [ros_gz_sim]: Entity creation successful.
[INFO] [create-4]: process has finished cleanly [pid 472]
[INFO] [spawner-6]: process started with pid [551]
[parameter_bridge-3] [INFO] [1791218120.419518200] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/clock (gz.msgs.Clock) -> /clock (rosgraph_msgs/msg/Clock)] (Lazy 0)
[parameter_bridge-3] [INFO] [1791218120.421523888] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/scan (gz.msgs.LaserScan) -> /scan (sensor_msgs/msg/LaserScan)] (Lazy 0)
[parameter_bridge-3] [INFO] [1791218120.424718602] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/camera/image_raw (gz.msgs.Image) -> /camera/image_raw (sensor_msgs/msg/Image)] (Lazy 0)
[parameter_bridge-3] [INFO] [1791218120.425618899] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/camera/camera_info (gz.msgs.CameraInfo) -> /camera/camera_info (sensor_msgs/msg/CameraInfo)] (Lazy 0)
[spawner-6] [INFO] [1791218120.935868354] [spawner_joint_state_broadcaster]: waiting for service /controller_manager/list_controllers to become available...
[gz-1] [1;33mWarning [Utils.cc:132][0m [/sdf/model[@name="vacuum"]/link[@name="camera_link"]/sensor[@name="camera"]/gz_frame_id:<urdf-string>:L0]: XML Element[gz_frame_id], child of element[sensor], not defined in SDF. Copying[gz_frame_id] as children of [sensor].
[gz-1] [1;33mWarning [Utils.cc:132][0m [/sdf/model[@name="vacuum"]/link[@name="lidar_link"]/sensor[@name="lidar"]/gz_frame_id:<urdf-string>:L0]: XML Element[gz_frame_id], child of element[sensor], not defined in SDF. Copying[gz_frame_id] as children of [sensor].
[gz-1] [INFO] [1791218121.935408622] [gz_ros_control]: [gz_ros2_control] Fixed joint ['camera_joint'] (Entity='53') is skipped.
[gz-1] [INFO] [1791218121.935607476] [gz_ros_control]: [gz_ros2_control] Fixed joint ['caster_joint'] (Entity='54') is skipped.
[gz-1] [INFO] [1791218121.935620923] [gz_ros_control]: [gz_ros2_control] Fixed joint ['lidar_joint'] (Entity='56') is skipped.
[gz-1] [INFO] [1791218121.940223569] [gz_ros_control]: Loading controller_manager
[gz-1] [INFO] [1791218121.983390746] [controller_manager]: Using ROS clock for triggering controller manager cycles.
[gz-1] [WARN] [1791218121.983476546] [controller_manager]: The resource manager is not yet initialized, will wait for the robot description to initialize it..
[gz-1] [INFO] [1791218122.000053247] [controller_manager]: Subscribing to '/robot_description' topic for robot description.
[gz-1] [WARN] [1791218122.000169593] [gz_ros_control]: Waiting RM to load and initialize hardware...
[gz-1] [WARN] [1791218123.000374037] [controller_manager]: Waiting for data on 'robot_description' topic to finish initialization
[gz-1] [INFO] [1791218123.438092691] [controller_manager]: Received robot description from topic.
[gz-1] [INFO] [1791218123.438318672] [controller_manager]: Enforcing command limits is disabled. Command limits from URDF will be ignored.
[gz-1] [INFO] [1791218123.444989264] [gz_ros_control]: The position_proportional_gain has been set to: 0.1
[gz-1] [INFO] [1791218123.445123477] [gz_ros_control]: Loading joint: left_wheel_joint
[gz-1] [INFO] [1791218123.445132838] [gz_ros_control]: 	State:
[gz-1] [INFO] [1791218123.445139207] [gz_ros_control]: 		 position
[gz-1] [INFO] [1791218123.445142832] [gz_ros_control]: 		 velocity
[gz-1] [INFO] [1791218123.445150745] [gz_ros_control]: 	Command:
[gz-1] [INFO] [1791218123.445154501] [gz_ros_control]: 		 velocity
[gz-1] [INFO] [1791218123.445166664] [gz_ros_control]: Loading joint: right_wheel_joint
[gz-1] [INFO] [1791218123.445169941] [gz_ros_control]: 	State:
[gz-1] [INFO] [1791218123.445172602] [gz_ros_control]: 		 position
[gz-1] [INFO] [1791218123.445176287] [gz_ros_control]: 		 velocity
[gz-1] [INFO] [1791218123.445179109] [gz_ros_control]: 	Command:
[gz-1] [INFO] [1791218123.445181627] [gz_ros_control]: 		 velocity
[gz-1] [INFO] [1791218123.445359191] [controller_manager]: Initialize hardware 'VacuumSimulation' 
[gz-1] [WARN] [1791218123.445389289] [controller_manager.hardware_component.system.VacuumSimulation]: Executor is not available during hardware component initialization for 'VacuumSimulation'. Skipping node creation!
[gz-1] [INFO] [1791218123.445573266] [controller_manager]: Successful initialization of hardware 'VacuumSimulation'
[gz-1] [INFO] [1791218123.445690966] [controller_manager]: Activating component 'VacuumSimulation'.
[gz-1] [INFO] [1791218123.445702353] [resource_manager]: 'configure' hardware 'VacuumSimulation' 
[gz-1] [INFO] [1791218123.445707743] [gz_ros_control]: System Successfully configured!
[gz-1] [INFO] [1791218123.445713706] [resource_manager]: Successful 'configure' of hardware 'VacuumSimulation'
[gz-1] [INFO] [1791218123.445720754] [resource_manager]: 'activate' hardware 'VacuumSimulation' 
[gz-1] [INFO] [1791218123.445737102] [resource_manager]: Successful 'activate' of hardware 'VacuumSimulation'
[gz-1] [WARN] [1791218123.445823133] [controller_manager]: Component 'VacuumSimulation' does not have read or write statistics initialized, skipping registration.
[gz-1] [INFO] [1791218123.445829106] [controller_manager]: Resource Manager has been successfully initialized. Starting Controller Manager services...
[gz-1] [WARN] [1791218124.062484808] [gz_ros_control]:  Desired controller update period (0.02 s) is slower than the gazebo simulation period (0.002 s).
[gz-1] [INFO] [1791218125.192536876] [controller_manager]: Loading controller : 'joint_state_broadcaster' of type 'joint_state_broadcaster/JointStateBroadcaster'
[gz-1] [INFO] [1791218125.192638547] [controller_manager]: Loading controller 'joint_state_broadcaster'
[gz-1] [WARN] [1791218125.204720293] [controller_manager]: The use of remapping arguments to the controller_manager node is deprecated. Please use the '--controller-ros-args' argument of the spawner to pass remapping arguments to the controller node.
[gz-1] [INFO] [1791218125.204818683] [controller_manager]: Controller 'joint_state_broadcaster' node arguments: --ros-args --params-file /home/robot/vacuum_ws/install/vacuum_sim/share/vacuum_sim/config/controllers.yaml --ros-args --remap /diff_drive_controller/odom:=/odom -p use_sim_time:=true --param use_sim_time:=true 
[spawner-6] [INFO] [1791218125.233536923] [spawner_joint_state_broadcaster]: Loaded joint_state_broadcaster
[gz-1] [INFO] [1791218125.236504603] [controller_manager]: Configuring controller: 'joint_state_broadcaster'
[gz-1] [INFO] [1791218125.236919164] [joint_state_broadcaster]: 'joints' or 'interfaces' parameter is empty. All available state interfaces will be published
[gz-1] [INFO] [1791218125.264260378] [controller_manager]: Activating controllers: [ joint_state_broadcaster ]
[gz-1] [1;33m[Wrn] [Ogre2Camera.cc:423] [0m[1;33mOgre2Camera::SetVisibilityMask: Mask bits [0m[1;33mc0000000[0m[1;33m are set but will be ignored as they conflict with the [0m[1;33mreserved bits used internally by the ogre2 backend.[0m[1;33m[0m
[gz-1] [INFO] [1791218126.750740836] [controller_manager]: Successfully switched controllers!
[spawner-6] [INFO] [1791218126.773101933] [spawner_joint_state_broadcaster]: Configured and activated joint_state_broadcaster
[gz-1] [INFO] [1791218126.774650370] [controller_manager]: Loading controller : 'diff_drive_controller' of type 'diff_drive_controller/DiffDriveController'
[gz-1] [INFO] [1791218126.774706647] [controller_manager]: Loading controller 'diff_drive_controller'
[gz-1] [WARN] [1791218126.783031636] [controller_manager]: The use of remapping arguments to the controller_manager node is deprecated. Please use the '--controller-ros-args' argument of the spawner to pass remapping arguments to the controller node.
[gz-1] [INFO] [1791218126.783109800] [controller_manager]: Controller 'diff_drive_controller' node arguments: --ros-args --params-file /home/robot/vacuum_ws/install/vacuum_sim/share/vacuum_sim/config/controllers.yaml --ros-args --remap /diff_drive_controller/odom:=/odom -p use_sim_time:=true --param use_sim_time:=true 
[spawner-6] [INFO] [1791218126.832456561] [spawner_joint_state_broadcaster]: Loaded diff_drive_controller
[gz-1] [INFO] [1791218126.833864012] [controller_manager]: Configuring controller: 'diff_drive_controller'
[gz-1] [INFO] [1791218126.851807052] [controller_manager]: Activating controllers: [ diff_drive_controller ]
[gz-1] [INFO] [1791218126.871241668] [controller_manager]: Successfully switched controllers!
[spawner-6] [INFO] [1791218126.893042111] [spawner_joint_state_broadcaster]: Configured and activated diff_drive_controller
[INFO] [spawner-6]: process has finished cleanly [pid 551]
[gz-1] [WARN] [1791218127.753498161] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218128.781179404] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218129.802965741] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218130.803068594] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218131.886032675] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218133.667149491] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218134.728339292] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218135.860243340] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218136.875591798] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218145.519102556] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218146.550265269] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218147.622573122] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218148.710425403] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218149.733861448] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218150.802498439] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218151.885535030] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218152.953514308] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218154.034452717] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218155.148202831] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218156.218363124] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218157.264987080] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218158.349876950] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218159.403138474] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218160.441679591] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218161.505105686] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218163.220937782] [diff_drive_controller]: Velocity command timed out. Braking.
[gz-1] [WARN] [1791218164.436349629] [diff_drive_controller]: Velocity command timed out. Braking.
[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[INFO] [twist_adapter.py-5]: sending signal 'SIGINT' to process[twist_adapter.py-5]
[INFO] [parameter_bridge-3]: sending signal 'SIGINT' to process[parameter_bridge-3]
[INFO] [robot_state_publisher-2]: sending signal 'SIGINT' to process[robot_state_publisher-2]
[INFO] [gz-1]: sending signal 'SIGINT' to process[gz-1]
[robot_state_publisher-2] [INFO] [1791218164.537760482] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[parameter_bridge-3] [INFO] [1791218164.538086172] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[parameter_bridge-3] [INFO] [1791218164.557617316] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[robot_state_publisher-2] [INFO] [1791218164.561648949] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [robot_state_publisher-2]: process has finished cleanly [pid 470]
[INFO] [parameter_bridge-3]: process has finished cleanly [pid 471]
[INFO] [twist_adapter.py-5]: process has finished cleanly [pid 473]
[ERROR] [gz-1]: process has died [pid 469, exit code -11, cmd 'gz sim -r -s -v 2 /home/robot/vacuum_ws/install/vacuum_sim/share/vacuum_sim/worlds/room.sdf'].


## validation/autonomy-20261006/isolated_guard.yaml

/autonomy_guard_test/collision_monitor:
  ros__parameters:
    FootprintApproach:
      action_type: approach
      enabled: true
      footprint_topic: /local_costmap/published_footprint
      min_points: 1
      simulation_time_step: 0.1
      time_before_collision: 1.2
      type: polygon
      visualize: false
    SlowZone:
      action_type: slowdown
      enabled: true
      min_points: 1
      points: '[[-0.37,-0.33],[0.42,-0.33],[0.42,0.33],[-0.37,0.33]]'
      polygon_pub_topic: /autonomy_guard_test/slow_polygon
      slowdown_ratio: 0.4
      type: polygon
      visualize: true
    StopZone:
      action_type: stop
      enabled: true
      min_points: 1
      points: '[[-0.29,-0.25],[0.22,-0.25],[0.22,0.25],[-0.29,0.25]]'
      polygon_pub_topic: /autonomy_guard_test/stop_polygon
      type: polygon
      visualize: true
    base_frame_id: base_footprint
    base_shift_correction: true
    cmd_vel_in_topic: /autonomy_guard_test/input
    cmd_vel_out_topic: /autonomy_guard_test/output
    enable_stamped_cmd_vel: false
    observation_sources:
    - scan
    odom_frame_id: odom
    polygons:
    - StopZone
    - SlowZone
    scan:
      enabled: true
      max_height: 2.0
      min_height: 0.0
      source_timeout: 0.5
      topic: /autonomy_guard_test/scan
      type: scan
    source_timeout: 0.5
    state_topic: /autonomy_guard_test/state
    stop_pub_timeout: 2.0
    transform_tolerance: 0.2
    use_sim_time: true


## validation/autonomy-20261006/navigation.log

[INFO] [launch]: All log files can be found below /home/robot/.ros/log/2026-10-06-00-35-31-507389-Justin-656
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [controller_server-1]: process started with pid [659]
[INFO] [smoother_server-2]: process started with pid [660]
[INFO] [planner_server-3]: process started with pid [661]
[INFO] [route_server-4]: process started with pid [662]
[INFO] [behavior_server-5]: process started with pid [663]
[INFO] [bt_navigator-6]: process started with pid [664]
[INFO] [waypoint_follower-7]: process started with pid [665]
[INFO] [velocity_smoother-8]: process started with pid [666]
[INFO] [collision_monitor-9]: process started with pid [667]
[INFO] [opennav_docking-10]: process started with pid [668]
[INFO] [lifecycle_manager-11]: process started with pid [669]
[velocity_smoother-8] [INFO] [1791218132.205499327] [velocity_smoother]: 
[velocity_smoother-8] 	velocity_smoother lifecycle node launched. 
[velocity_smoother-8] 	Waiting on external lifecycle transitions to activate
[velocity_smoother-8] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[behavior_server-5] [INFO] [1791218132.637384055] [behavior_server]: 
[behavior_server-5] 	behavior_server lifecycle node launched. 
[behavior_server-5] 	Waiting on external lifecycle transitions to activate
[behavior_server-5] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[route_server-4] [INFO] [1791218132.728922938] [route_server]: 
[route_server-4] 	route_server lifecycle node launched. 
[route_server-4] 	Waiting on external lifecycle transitions to activate
[route_server-4] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[smoother_server-2] [INFO] [1791218132.754590279] [smoother_server]: 
[smoother_server-2] 	smoother_server lifecycle node launched. 
[smoother_server-2] 	Waiting on external lifecycle transitions to activate
[smoother_server-2] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[smoother_server-2] [INFO] [1791218132.761836395] [smoother_server]: Creating smoother server
[opennav_docking-10] [INFO] [1791218132.817336497] [docking_server]: 
[opennav_docking-10] 	docking_server lifecycle node launched. 
[opennav_docking-10] 	Waiting on external lifecycle transitions to activate
[opennav_docking-10] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[opennav_docking-10] [INFO] [1791218132.819364755] [docking_server]: Creating docking_server
[planner_server-3] [INFO] [1791218133.037973576] [planner_server]: 
[planner_server-3] 	planner_server lifecycle node launched. 
[planner_server-3] 	Waiting on external lifecycle transitions to activate
[planner_server-3] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[lifecycle_manager-11] [INFO] [1791218133.042276252] [lifecycle_manager_navigation]: Creating
[planner_server-3] [INFO] [1791218133.046497235] [planner_server]: Creating
[waypoint_follower-7] [INFO] [1791218133.068029496] [waypoint_follower]: 
[waypoint_follower-7] 	waypoint_follower lifecycle node launched. 
[waypoint_follower-7] 	Waiting on external lifecycle transitions to activate
[waypoint_follower-7] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[waypoint_follower-7] [INFO] [1791218133.088324166] [waypoint_follower]: Creating
[collision_monitor-9] [INFO] [1791218133.138235146] [collision_monitor]: 
[collision_monitor-9] 	collision_monitor lifecycle node launched. 
[collision_monitor-9] 	Waiting on external lifecycle transitions to activate
[collision_monitor-9] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[controller_server-1] [INFO] [1791218133.145102848] [controller_server]: 
[controller_server-1] 	controller_server lifecycle node launched. 
[controller_server-1] 	Waiting on external lifecycle transitions to activate
[controller_server-1] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[controller_server-1] [INFO] [1791218133.167158732] [controller_server]: Creating controller server
[lifecycle_manager-11] [INFO] [1791218133.213966036] [lifecycle_manager_navigation]: [34m[1mCreating and initializing lifecycle service clients[0m[0m
[bt_navigator-6] [INFO] [1791218133.268162898] [bt_navigator]: 
[bt_navigator-6] 	bt_navigator lifecycle node launched. 
[bt_navigator-6] 	Waiting on external lifecycle transitions to activate
[bt_navigator-6] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[bt_navigator-6] [INFO] [1791218133.272344823] [bt_navigator]: Creating
[controller_server-1] [INFO] [1791218133.342159618] [local_costmap.local_costmap]: 
[controller_server-1] 	local_costmap lifecycle node launched. 
[controller_server-1] 	Waiting on external lifecycle transitions to activate
[controller_server-1] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[controller_server-1] [INFO] [1791218133.346702532] [local_costmap.local_costmap]: Creating Costmap
[planner_server-3] [INFO] [1791218133.359148184] [global_costmap.global_costmap]: 
[planner_server-3] 	global_costmap lifecycle node launched. 
[planner_server-3] 	Waiting on external lifecycle transitions to activate
[planner_server-3] 	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[planner_server-3] [INFO] [1791218133.360441123] [global_costmap.global_costmap]: Creating Costmap
[lifecycle_manager-11] [INFO] [1791218133.995737625] [lifecycle_manager_navigation]: [34m[1mStarting managed nodes bringup...[0m[0m
[lifecycle_manager-11] [INFO] [1791218133.995829104] [lifecycle_manager_navigation]: [34m[1mConfiguring controller_server[0m[0m
[controller_server-1] [INFO] [1791218133.996330460] [controller_server]: Configuring controller interface
[controller_server-1] [INFO] [1791218133.996351657] [controller_server]: getting progress checker plugins..
[controller_server-1] [INFO] [1791218133.996595103] [controller_server]: getting goal checker plugins..
[controller_server-1] [INFO] [1791218133.996680343] [controller_server]: Controller frequency set to 20.0000Hz
[controller_server-1] [INFO] [1791218133.996719555] [local_costmap.local_costmap]: Configuring
[controller_server-1] [INFO] [1791218134.016600795] [local_costmap.local_costmap]: Using plugin "obstacle_layer"
[controller_server-1] [INFO] [1791218134.027387028] [local_costmap.local_costmap]: Subscribed to Topics: scan
[controller_server-1] [INFO] [1791218134.034273184] [local_costmap.local_costmap]: Initialized plugin "obstacle_layer"
[controller_server-1] [INFO] [1791218134.034364963] [local_costmap.local_costmap]: Using plugin "inflation_layer"
[controller_server-1] [INFO] [1791218134.035684083] [local_costmap.local_costmap]: Initialized plugin "inflation_layer"
[controller_server-1] [INFO] [1791218134.094471128] [controller_server]: Created progress_checker : progress_checker of type nav2_controller::SimpleProgressChecker
[controller_server-1] [INFO] [1791218134.095254010] [controller_server]: Controller Server has progress_checker  progress checkers available.
[controller_server-1] [INFO] [1791218134.097148005] [controller_server]: Created goal checker : general_goal_checker of type nav2_controller::SimpleGoalChecker
[controller_server-1] [INFO] [1791218134.098491701] [controller_server]: Controller Server has general_goal_checker  goal checkers available.
[controller_server-1] [INFO] [1791218134.114387034] [controller_server]: Created controller : FollowPath of type dwb_core::DWBLocalPlanner
[controller_server-1] [INFO] [1791218134.115160497] [controller_server]: Setting transform_tolerance to 0.200000
[controller_server-1] [INFO] [1791218134.155509856] [controller_server]: Using critic "RotateToGoal" (dwb_critics::RotateToGoalCritic)
[controller_server-1] [INFO] [1791218134.157063175] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1791218134.157301813] [controller_server]: Using critic "Oscillation" (dwb_critics::OscillationCritic)
[controller_server-1] [INFO] [1791218134.157648309] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1791218134.157778153] [controller_server]: Using critic "ObstacleFootprint" (dwb_critics::ObstacleFootprintCritic)
[controller_server-1] [INFO] [1791218134.157914790] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1791218134.158031178] [controller_server]: Using critic "GoalAlign" (dwb_critics::GoalAlignCritic)
[controller_server-1] [INFO] [1791218134.158491845] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1791218134.158592894] [controller_server]: Using critic "PathAlign" (dwb_critics::PathAlignCritic)
[controller_server-1] [INFO] [1791218134.158842002] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1791218134.158961098] [controller_server]: Using critic "PathDist" (dwb_critics::PathDistCritic)
[controller_server-1] [INFO] [1791218134.161073028] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1791218134.162134114] [controller_server]: Using critic "GoalDist" (dwb_critics::GoalDistCritic)
[controller_server-1] [INFO] [1791218134.163002738] [controller_server]: Critic plugin initialized
[controller_server-1] [INFO] [1791218134.163053728] [controller_server]: Controller Server has FollowPath  controllers available.
[lifecycle_manager-11] [INFO] [1791218134.201187523] [lifecycle_manager_navigation]: [34m[1mConfiguring smoother_server[0m[0m
[smoother_server-2] [INFO] [1791218134.201827918] [smoother_server]: Configuring smoother server
[smoother_server-2] [INFO] [1791218134.241511902] [smoother_server]: Created smoother : simple_smoother of type nav2_smoother::SimpleSmoother
[smoother_server-2] [INFO] [1791218134.242157073] [smoother_server]: Smoother Server has simple_smoother  smoothers available.
[lifecycle_manager-11] [INFO] [1791218134.273272472] [lifecycle_manager_navigation]: [34m[1mConfiguring planner_server[0m[0m
[planner_server-3] [INFO] [1791218134.273976666] [planner_server]: Configuring
[planner_server-3] [INFO] [1791218134.274035779] [global_costmap.global_costmap]: Configuring
[planner_server-3] [INFO] [1791218134.313325270] [global_costmap.global_costmap]: Using plugin "static_layer"
[planner_server-3] [INFO] [1791218134.320282330] [global_costmap.global_costmap]: Subscribing to the map topic (/map) with transient local durability
[planner_server-3] [INFO] [1791218134.325342556] [global_costmap.global_costmap]: Initialized plugin "static_layer"
[planner_server-3] [INFO] [1791218134.325407210] [global_costmap.global_costmap]: Using plugin "obstacle_layer"
[planner_server-3] [INFO] [1791218134.327528869] [global_costmap.global_costmap]: Subscribed to Topics: scan
[planner_server-3] [INFO] [1791218134.338005059] [global_costmap.global_costmap]: Initialized plugin "obstacle_layer"
[planner_server-3] [INFO] [1791218134.338099058] [global_costmap.global_costmap]: Using plugin "inflation_layer"
[planner_server-3] [INFO] [1791218134.342137515] [global_costmap.global_costmap]: Initialized plugin "inflation_layer"
[planner_server-3] [INFO] [1791218134.408614780] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 119 X 119 at 0.050000 m/pix
[planner_server-3] [INFO] [1791218134.411270486] [planner_server]: Created global planner plugin GridBased of type nav2_navfn_planner::NavfnPlanner
[planner_server-3] [INFO] [1791218134.411381299] [planner_server]: Configuring plugin GridBased of type NavfnPlanner
[planner_server-3] [INFO] [1791218134.412583884] [planner_server]: Planner Server has GridBased  planners available.
[lifecycle_manager-11] [INFO] [1791218134.455477424] [lifecycle_manager_navigation]: [34m[1mConfiguring route_server[0m[0m
[route_server-4] [INFO] [1791218134.455927272] [route_server]: Configuring
[route_server-4] [INFO] [1791218134.552277547] [route_server]: Created GraphFileLoader GeoJsonGraphFileLoader of type nav2_route::GeoJsonGraphFileLoader
[route_server-4] [INFO] [1791218134.552345377] [route_server]: Configuring geojson graph file loader
[route_server-4] [INFO] [1791218134.552355182] [route_server]: No graph file provided to load yet.
[route_server-4] [INFO] [1791218134.557808955] [route_server]: Created edge cost function plugin DistanceScorer of type nav2_route::DistanceScorer
[route_server-4] [INFO] [1791218134.557883649] [route_server]: Configuring distance scorer.
[route_server-4] [INFO] [1791218134.558705326] [route_server]: Created edge cost function plugin CostmapScorer of type nav2_route::CostmapScorer
[route_server-4] [INFO] [1791218134.558739364] [route_server]: Configuring costmap scorer.
[route_server-4] [INFO] [1791218134.562355855] [route_server]: Created route operation AdjustSpeedLimit of type nav2_route::AdjustSpeedLimit
[route_server-4] [INFO] [1791218134.562440590] [route_server]: Configuring Adjust speed limit operation.
[route_server-4] [INFO] [1791218134.567351511] [route_server]: Created route operation ReroutingService of type nav2_route::ReroutingService
[route_server-4] [INFO] [1791218134.567415772] [route_server]: Configuring Rerouting service operation.
[route_server-4] [INFO] [1791218134.573581879] [route_server]: Created route operation CollisionMonitor of type nav2_route::CollisionMonitor
[route_server-4] [INFO] [1791218134.574397503] [route_server]: Using costmap topic: local_costmap/costmap_raw instead of server costmap topic: global_costmap/costmap_raw for CollisionMonitor.
[lifecycle_manager-11] [INFO] [1791218134.584946047] [lifecycle_manager_navigation]: [34m[1mConfiguring behavior_server[0m[0m
[behavior_server-5] [INFO] [1791218134.585541329] [behavior_server]: Configuring
[behavior_server-5] [INFO] [1791218134.602426322] [behavior_server]: Creating behavior plugin wait of type nav2_behaviors::Wait
[behavior_server-5] [INFO] [1791218134.631697609] [behavior_server]: Configuring wait
[lifecycle_manager-11] [INFO] [1791218134.664272616] [lifecycle_manager_navigation]: [34m[1mConfiguring velocity_smoother[0m[0m
[velocity_smoother-8] [INFO] [1791218134.665127561] [velocity_smoother]: Configuring velocity smoother
[lifecycle_manager-11] [INFO] [1791218134.685850586] [lifecycle_manager_navigation]: [34m[1mConfiguring collision_monitor[0m[0m
[collision_monitor-9] [INFO] [1791218134.686431078] [collision_monitor]: Configuring
[collision_monitor-9] [INFO] [1791218134.708360557] [collision_monitor]: [scan]: Creating Scan
[collision_monitor-9] [INFO] [1791218134.716636160] [collision_monitor]: [StopZone]: Creating Polygon
[collision_monitor-9] [INFO] [1791218134.722898811] [collision_monitor]: [SlowZone]: Creating Polygon
[collision_monitor-9] [INFO] [1791218134.729993889] [collision_monitor]: [FootprintApproach]: Creating Polygon
[collision_monitor-9] [INFO] [1791218134.730126883] [collision_monitor]: [FootprintApproach]: Polygon points are not defined. Using dynamic subscription instead.
[collision_monitor-9] [INFO] [1791218134.739055860] [collision_monitor]: [FootprintApproach]: Making footprint subscriber on /local_costmap/published_footprint topic
[lifecycle_manager-11] [INFO] [1791218134.773748003] [lifecycle_manager_navigation]: [34m[1mConfiguring bt_navigator[0m[0m
[bt_navigator-6] [INFO] [1791218134.774239122] [bt_navigator]: Configuring
[bt_navigator-6] [INFO] [1791218134.789230400] [bt_navigator]: Creating navigator id navigate_to_pose of type nav2_bt_navigator::NavigateToPoseNavigator
[lifecycle_manager-11] [INFO] [1791218135.113146394] [lifecycle_manager_navigation]: [34m[1mConfiguring waypoint_follower[0m[0m
[waypoint_follower-7] [INFO] [1791218135.114677852] [waypoint_follower]: Configuring
[waypoint_follower-7] [INFO] [1791218135.231320371] [waypoint_follower]: Created waypoint_task_executor : wait_at_waypoint of type nav2_waypoint_follower::WaitAtWaypoint
[lifecycle_manager-11] [INFO] [1791218135.235642235] [lifecycle_manager_navigation]: [34m[1mConfiguring docking_server[0m[0m
[opennav_docking-10] [INFO] [1791218135.237353619] [docking_server]: Configuring docking_server
[opennav_docking-10] [INFO] [1791218135.238676719] [docking_server]: Controller frequency set to 50.0000Hz
[opennav_docking-10] [INFO] [1791218135.427405352] [docking_server]: Created charging dock plugin simple_charging_dock of type opennav_docking::SimpleChargingDock
[opennav_docking-10] [WARN] [1791218135.464497311] [docking_server]: Dock database filepath nor dock parameters set. Docking actions can only be executed specifying the dock pose via the action request. Or update the dock database via the reload_database service.
[opennav_docking-10] [INFO] [1791218135.464583216] [docking_server]: Docking Server has 1 dock types and 0 dock instances available.
[lifecycle_manager-11] [INFO] [1791218135.486052669] [lifecycle_manager_navigation]: [34m[1mActivating controller_server[0m[0m
[controller_server-1] [INFO] [1791218135.493454406] [controller_server]: Activating
[controller_server-1] [INFO] [1791218135.493533772] [local_costmap.local_costmap]: Activating
[controller_server-1] [INFO] [1791218135.493544786] [local_costmap.local_costmap]: Checking transform
[controller_server-1] [INFO] [1791218135.493813322] [local_costmap.local_costmap]: start
[controller_server-1] [INFO] [1791218135.701792767] [controller_server]: Creating bond (controller_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1791218135.819614741] [lifecycle_manager_navigation]: Server controller_server connected with bond.
[lifecycle_manager-11] [INFO] [1791218135.819693960] [lifecycle_manager_navigation]: [34m[1mActivating smoother_server[0m[0m
[smoother_server-2] [INFO] [1791218135.820272566] [smoother_server]: Activating
[smoother_server-2] [INFO] [1791218135.820330550] [smoother_server]: Creating bond (smoother_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1791218135.939191686] [lifecycle_manager_navigation]: Server smoother_server connected with bond.
[lifecycle_manager-11] [INFO] [1791218135.939291361] [lifecycle_manager_navigation]: [34m[1mActivating planner_server[0m[0m
[planner_server-3] [INFO] [1791218135.941015713] [planner_server]: Activating
[planner_server-3] [INFO] [1791218135.941082327] [global_costmap.global_costmap]: Activating
[planner_server-3] [INFO] [1791218135.941093160] [global_costmap.global_costmap]: Checking transform
[planner_server-3] [INFO] [1791218135.941413516] [global_costmap.global_costmap]: start
[planner_server-3] [INFO] [1791218136.947773176] [planner_server]: Activating plugin GridBased of type NavfnPlanner
[planner_server-3] [INFO] [1791218136.957455804] [planner_server]: Creating bond (planner_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1791218137.067267044] [lifecycle_manager_navigation]: Server planner_server connected with bond.
[lifecycle_manager-11] [INFO] [1791218137.067384622] [lifecycle_manager_navigation]: [34m[1mActivating route_server[0m[0m
[route_server-4] [INFO] [1791218137.068095555] [route_server]: Activating
[route_server-4] [INFO] [1791218137.068362302] [route_server]: Creating bond (route_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1791218137.206243111] [lifecycle_manager_navigation]: Server route_server connected with bond.
[lifecycle_manager-11] [INFO] [1791218137.206393651] [lifecycle_manager_navigation]: [34m[1mActivating behavior_server[0m[0m
[behavior_server-5] [INFO] [1791218137.207865489] [behavior_server]: Activating
[behavior_server-5] [INFO] [1791218137.207937188] [behavior_server]: Activating wait
[behavior_server-5] [INFO] [1791218137.207962536] [behavior_server]: Creating bond (behavior_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1791218137.331090060] [lifecycle_manager_navigation]: Server behavior_server connected with bond.
[lifecycle_manager-11] [INFO] [1791218137.331168727] [lifecycle_manager_navigation]: [34m[1mActivating velocity_smoother[0m[0m
[velocity_smoother-8] [INFO] [1791218137.332143421] [velocity_smoother]: Activating
[velocity_smoother-8] [INFO] [1791218137.332248155] [velocity_smoother]: Creating bond (velocity_smoother) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1791218137.456874775] [lifecycle_manager_navigation]: Server velocity_smoother connected with bond.
[lifecycle_manager-11] [INFO] [1791218137.457039943] [lifecycle_manager_navigation]: [34m[1mActivating collision_monitor[0m[0m
[collision_monitor-9] [INFO] [1791218137.458279261] [collision_monitor]: Activating
[collision_monitor-9] [INFO] [1791218137.458532340] [collision_monitor]: Creating bond (collision_monitor) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1791218137.579167335] [lifecycle_manager_navigation]: Server collision_monitor connected with bond.
[lifecycle_manager-11] [INFO] [1791218137.579238272] [lifecycle_manager_navigation]: [34m[1mActivating bt_navigator[0m[0m
[bt_navigator-6] [INFO] [1791218137.579780102] [bt_navigator]: Activating
[bt_navigator-6] [INFO] [1791218137.693639348] [bt_navigator]: Creating bond (bt_navigator) to lifecycle manager.
[bt_navigator-6] [INFO] [1791218137.781246253] [bt_navigator]: Begin navigating from current location (0.00, 0.00) to (1.00, 0.00)
[lifecycle_manager-11] [INFO] [1791218137.818404687] [lifecycle_manager_navigation]: Server bt_navigator connected with bond.
[lifecycle_manager-11] [INFO] [1791218137.818459604] [lifecycle_manager_navigation]: [34m[1mActivating waypoint_follower[0m[0m
[controller_server-1] [INFO] [1791218137.818352634] [controller_server]: Received a goal, begin computing control effort.
[controller_server-1] [WARN] [1791218137.818462152] [controller_server]: No goal checker was specified in parameter 'current_goal_checker'. Server will use only plugin loaded general_goal_checker . This warning will appear once.
[controller_server-1] [WARN] [1791218137.818475289] [controller_server]: No progress checker was specified in parameter 'current_progress_checker'. Server will use only plugin loaded progress_checker . This warning will appear once.
[waypoint_follower-7] [INFO] [1791218137.819301345] [waypoint_follower]: Activating
[waypoint_follower-7] [INFO] [1791218137.819363021] [waypoint_follower]: Creating bond (waypoint_follower) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1791218137.960496691] [lifecycle_manager_navigation]: Server waypoint_follower connected with bond.
[lifecycle_manager-11] [INFO] [1791218137.960582351] [lifecycle_manager_navigation]: [34m[1mActivating docking_server[0m[0m
[opennav_docking-10] [INFO] [1791218137.961979589] [docking_server]: Activating docking_server
[opennav_docking-10] [INFO] [1791218138.034166911] [docking_server]: Creating bond (docking_server) to lifecycle manager.
[lifecycle_manager-11] [INFO] [1791218138.149148581] [lifecycle_manager_navigation]: Server docking_server connected with bond.
[lifecycle_manager-11] [INFO] [1791218138.149256404] [lifecycle_manager_navigation]: [34m[1mManaged nodes are active[0m[0m
[lifecycle_manager-11] [INFO] [1791218138.149270041] [lifecycle_manager_navigation]: [34m[1mCreating bond timer...[0m[0m
[controller_server-1] [INFO] [1791218138.869255511] [controller_server]: Passing new path to controller.
[controller_server-1] [INFO] [1791218139.869252512] [controller_server]: Passing new path to controller.
[controller_server-1] [INFO] [1791218140.920130653] [controller_server]: Passing new path to controller.
[planner_server-3] [INFO] [1791218140.944089548] [global_costmap.global_costmap]: StaticLayer: Resizing costmap to 119 X 119 at 0.050000 m/pix
[controller_server-1] [INFO] [1791218141.919207956] [controller_server]: Passing new path to controller.
[controller_server-1] [INFO] [1791218142.919395522] [controller_server]: Passing new path to controller.
[controller_server-1] [INFO] [1791218143.969458156] [controller_server]: Passing new path to controller.
[controller_server-1] [INFO] [1791218144.519319761] [controller_server]: Reached the goal!
[bt_navigator-6] [INFO] [1791218144.543718482] [bt_navigator]: Goal succeeded
[bt_navigator-6] [INFO] [1791218144.544449198] [bt_navigator]: Begin navigating from current location (0.90, -0.01) to (3.15, 0.00)
[planner_server-3] [WARN] [1791218144.545606880] [planner_server]: GridBased plugin failed to plan from (0.90, -0.01) to (3.15, 0.00): "Goal Coordinates of(3.150000, 0.000000) was outside bounds"
[planner_server-3] [WARN] [1791218144.545671096] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[behavior_server-5] [INFO] [1791218144.566701269] [behavior_server]: Running wait
[behavior_server-5] [INFO] [1791218147.767150251] [behavior_server]: wait completed successfully
[planner_server-3] [WARN] [1791218147.785632072] [planner_server]: GridBased plugin failed to plan from (0.90, -0.01) to (3.15, 0.00): "Goal Coordinates of(3.150000, 0.000000) was outside bounds"
[planner_server-3] [WARN] [1791218147.785737739] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[behavior_server-5] [INFO] [1791218147.795754108] [behavior_server]: Running wait
[behavior_server-5] [INFO] [1791218150.997323924] [behavior_server]: wait completed successfully
[planner_server-3] [WARN] [1791218151.015754063] [planner_server]: GridBased plugin failed to plan from (0.90, -0.01) to (3.15, 0.00): "Goal Coordinates of(3.150000, 0.000000) was outside bounds"
[planner_server-3] [WARN] [1791218151.015874402] [planner_server]: [compute_path_to_pose] [ActionServer] Aborting handle.
[bt_navigator-6] [WARN] [1791218151.034684839] [bt_navigator]: [navigate_to_pose] [ActionServer] Aborting handle.
[bt_navigator-6] [ERROR] [1791218151.035311889] [bt_navigator]: Goal failed
[WARNING] [launch]: user interrupted with ctrl-c (SIGINT)
[opennav_docking-10] [INFO] [1791218161.663500044] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[opennav_docking-10] [INFO] [1791218161.663664417] [docking_server]: Running Nav2 LifecycleNode rcl preshutdown (docking_server)
[opennav_docking-10] [INFO] [1791218161.663742727] [docking_server]: Deactivating docking_server
[waypoint_follower-7] [INFO] [1791218161.663535885] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[waypoint_follower-7] [INFO] [1791218161.663637487] [waypoint_follower]: Running Nav2 LifecycleNode rcl preshutdown (waypoint_follower)
[waypoint_follower-7] [INFO] [1791218161.663742360] [waypoint_follower]: Deactivating
[waypoint_follower-7] [INFO] [1791218161.663771789] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[collision_monitor-9] [INFO] [1791218161.663575035] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[collision_monitor-9] [INFO] [1791218161.663775547] [collision_monitor]: Running Nav2 LifecycleNode rcl preshutdown (collision_monitor)
[collision_monitor-9] [INFO] [1791218161.663856881] [collision_monitor]: Deactivating
[collision_monitor-9] [INFO] [1791218161.663881652] [collision_monitor]: Destroying bond (collision_monitor) to lifecycle manager.
[collision_monitor-9] [INFO] [1791218161.674648725] [collision_monitor]: Cleaning up
[collision_monitor-9] [INFO] [1791218161.674719879] [collision_monitor]: [StopZone]: Destroying Polygon
[collision_monitor-9] [INFO] [1791218161.674734882] [collision_monitor]: [SlowZone]: Destroying Polygon
[collision_monitor-9] [INFO] [1791218161.674743154] [collision_monitor]: [FootprintApproach]: Destroying Polygon
[collision_monitor-9] [INFO] [1791218161.674753775] [collision_monitor]: [scan]: Destroying Scan
[lifecycle_manager-11] [INFO] [1791218161.663602113] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-11] [INFO] [1791218161.663756274] [lifecycle_manager_navigation]: Running Nav2 LifecycleManager rcl preshutdown (lifecycle_manager_navigation)
[lifecycle_manager-11] [INFO] [1791218161.664238579] [lifecycle_manager_navigation]: [34m[1mTerminating bond timer...[0m[0m
[route_server-4] [INFO] [1791218161.664185323] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[route_server-4] [INFO] [1791218161.664269932] [route_server]: Running Nav2 LifecycleNode rcl preshutdown (route_server)
[route_server-4] [INFO] [1791218161.664325438] [route_server]: Deactivating
[route_server-4] [INFO] [1791218161.664342187] [route_server]: Destroying bond (route_server) to lifecycle manager.
[planner_server-3] [INFO] [1791218161.664468526] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[planner_server-3] [INFO] [1791218161.664535815] [planner_server]: Running Nav2 LifecycleNode rcl preshutdown (planner_server)
[planner_server-3] [INFO] [1791218161.664600975] [planner_server]: Deactivating
[planner_server-3] [INFO] [1791218161.664637782] [global_costmap.global_costmap]: Deactivating
[smoother_server-2] [INFO] [1791218161.664496685] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[smoother_server-2] [INFO] [1791218161.664581974] [smoother_server]: Running Nav2 LifecycleNode rcl preshutdown (smoother_server)
[smoother_server-2] [INFO] [1791218161.664633102] [smoother_server]: Deactivating
[smoother_server-2] [INFO] [1791218161.664652905] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[bt_navigator-6] [INFO] [1791218161.664824361] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[bt_navigator-6] [INFO] [1791218161.664888720] [bt_navigator]: Running Nav2 LifecycleNode rcl preshutdown (bt_navigator)
[bt_navigator-6] [INFO] [1791218161.665448606] [bt_navigator]: Deactivating
[bt_navigator-6] [INFO] [1791218161.665540632] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[INFO] [lifecycle_manager-11]: sending signal 'SIGINT' to process[lifecycle_manager-11]
[INFO] [opennav_docking-10]: sending signal 'SIGINT' to process[opennav_docking-10]
[INFO] [collision_monitor-9]: sending signal 'SIGINT' to process[collision_monitor-9]
[INFO] [velocity_smoother-8]: sending signal 'SIGINT' to process[velocity_smoother-8]
[INFO] [waypoint_follower-7]: sending signal 'SIGINT' to process[waypoint_follower-7]
[INFO] [bt_navigator-6]: sending signal 'SIGINT' to process[bt_navigator-6]
[INFO] [behavior_server-5]: sending signal 'SIGINT' to process[behavior_server-5]
[INFO] [route_server-4]: sending signal 'SIGINT' to process[route_server-4]
[INFO] [planner_server-3]: sending signal 'SIGINT' to process[planner_server-3]
[INFO] [smoother_server-2]: sending signal 'SIGINT' to process[smoother_server-2]
[INFO] [controller_server-1]: sending signal 'SIGINT' to process[controller_server-1]
[waypoint_follower-7] [INFO] [1791218161.684447472] [waypoint_follower]: Cleaning up
[collision_monitor-9] [INFO] [1791218161.684539907] [collision_monitor]: Destroying bond (collision_monitor) to lifecycle manager.
[route_server-4] [INFO] [1791218161.685465205] [route_server]: Cleaning up
[smoother_server-2] [INFO] [1791218161.685639296] [smoother_server]: Cleaning up
[behavior_server-5] [INFO] [1791218161.678224416] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[behavior_server-5] [INFO] [1791218161.678327028] [behavior_server]: Running Nav2 LifecycleNode rcl preshutdown (behavior_server)
[behavior_server-5] [INFO] [1791218161.678407593] [behavior_server]: Deactivating
[behavior_server-5] [INFO] [1791218161.678435390] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[controller_server-1] [INFO] [1791218161.678759398] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[controller_server-1] [INFO] [1791218161.678896091] [controller_server]: Running Nav2 LifecycleNode rcl preshutdown (controller_server)
[controller_server-1] [INFO] [1791218161.678969277] [controller_server]: Deactivating
[controller_server-1] [INFO] [1791218161.679021724] [local_costmap.local_costmap]: Deactivating
[velocity_smoother-8] [INFO] [1791218161.679007757] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[velocity_smoother-8] [INFO] [1791218161.679144242] [velocity_smoother]: Running Nav2 LifecycleNode rcl preshutdown (velocity_smoother)
[velocity_smoother-8] [INFO] [1791218161.679257050] [velocity_smoother]: Deactivating
[velocity_smoother-8] [INFO] [1791218161.679290752] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[bt_navigator-6] [INFO] [1791218161.688223746] [bt_navigator]: Cleaning up
[controller_server-1] [INFO] [1791218161.697184399] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[velocity_smoother-8] [INFO] [1791218161.712366397] [velocity_smoother]: Cleaning up
[velocity_smoother-8] [INFO] [1791218161.712424214] [velocity_smoother]: Destroying bond (velocity_smoother) to lifecycle manager.
[controller_server-1] [INFO] [1791218161.717586577] [controller_server]: Cleaning up
[controller_server-1] [INFO] [1791218161.721926728] [local_costmap.local_costmap]: Cleaning up
[behavior_server-5] [INFO] [1791218161.719178189] [behavior_server]: Cleaning up
[opennav_docking-10] [INFO] [1791218161.745815430] [docking_server]: Destroying bond (docking_server) to lifecycle manager.
[collision_monitor-9] [INFO] [1791218161.756031286] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[velocity_smoother-8] [INFO] [1791218161.756821859] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[velocity_smoother-8] [INFO] [1791218161.774124203] [velocity_smoother]: Destroying
[opennav_docking-10] [INFO] [1791218161.776716809] [docking_server]: Cleaning up docking_server
[smoother_server-2] [INFO] [1791218161.813761959] [smoother_server]: Destroying bond (smoother_server) to lifecycle manager.
[waypoint_follower-7] [INFO] [1791218161.820289155] [waypoint_follower]: Destroying bond (waypoint_follower) to lifecycle manager.
[waypoint_follower-7] [INFO] [1791218161.827988566] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[smoother_server-2] [INFO] [1791218161.832426679] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[smoother_server-2] [INFO] [1791218161.836306192] [smoother_server]: Destroying
[waypoint_follower-7] [INFO] [1791218161.832622143] [waypoint_follower]: Destroying
[behavior_server-5] [INFO] [1791218161.849103266] [behavior_server]: Destroying bond (behavior_server) to lifecycle manager.
[route_server-4] [INFO] [1791218161.855703550] [route_server]: Destroying bond (route_server) to lifecycle manager.
[behavior_server-5] [INFO] [1791218161.857764161] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[collision_monitor-9] [INFO] [1791218161.860978870] [collision_monitor]: Destroying
[route_server-4] [INFO] [1791218161.868595572] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[behavior_server-5] [INFO] [1791218161.885279041] [behavior_server]: Destroying
[opennav_docking-10] [INFO] [1791218161.903721401] [docking_server]: Destroying bond (docking_server) to lifecycle manager.
[opennav_docking-10] [INFO] [1791218161.909284036] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[opennav_docking-10] [INFO] [1791218161.934176603] [docking_server]: Destroying
[planner_server-3] [INFO] [1791218161.944321275] [planner_server]: Deactivating plugin GridBased of type NavfnPlanner
[planner_server-3] [INFO] [1791218161.944424287] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[planner_server-3] [INFO] [1791218161.954640586] [planner_server]: Cleaning up
[route_server-4] [INFO] [1791218161.971385138] [route_server]: Destroying
[bt_navigator-6] [INFO] [1791218162.053302762] [bt_navigator]: Completed Cleaning up
[bt_navigator-6] [INFO] [1791218162.053403019] [bt_navigator]: Destroying bond (bt_navigator) to lifecycle manager.
[bt_navigator-6] [INFO] [1791218162.059271469] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [velocity_smoother-8]: process has finished cleanly [pid 666]
[controller_server-1] [INFO] [1791218162.076987547] [controller_server]: Destroying bond (controller_server) to lifecycle manager.
[planner_server-3] [INFO] [1791218162.093673267] [global_costmap.global_costmap]: Cleaning up
[controller_server-1] [INFO] [1791218162.095761666] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[lifecycle_manager-11] [INFO] [1791218162.116816036] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[bt_navigator-6] [INFO] [1791218162.116906293] [bt_navigator]: Destroying
[planner_server-3] [INFO] [1791218162.148906554] [planner_server]: Cleaning up plugin GridBased of type NavfnPlanner
[planner_server-3] [INFO] [1791218162.164934082] [planner_server]: Destroying plugin GridBased of type NavfnPlanner
[INFO] [collision_monitor-9]: process has finished cleanly [pid 667]
[lifecycle_manager-11] [INFO] [1791218162.177126317] [lifecycle_manager_navigation]: Destroying lifecycle_manager_navigation
[INFO] [smoother_server-2]: process has finished cleanly [pid 660]
[controller_server-1] [INFO] [1791218162.185417028] [local_costmap.local_costmap]: Destroying
[INFO] [waypoint_follower-7]: process has finished cleanly [pid 665]
[INFO] [behavior_server-5]: process has finished cleanly [pid 663]
[INFO] [route_server-4]: process has finished cleanly [pid 662]
[INFO] [opennav_docking-10]: process has finished cleanly [pid 668]
[controller_server-1] [INFO] [1791218162.398982468] [controller_server]: Destroying
[planner_server-3] [INFO] [1791218162.421268081] [planner_server]: Destroying bond (planner_server) to lifecycle manager.
[planner_server-3] [INFO] [1791218162.433055040] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[planner_server-3] [INFO] [1791218162.443684098] [global_costmap.global_costmap]: Destroying
[INFO] [lifecycle_manager-11]: process has finished cleanly [pid 669]
[planner_server-3] [INFO] [1791218162.515453304] [planner_server]: Destroying
[INFO] [bt_navigator-6]: process has finished cleanly [pid 664]
[INFO] [controller_server-1]: process has finished cleanly [pid 659]
[INFO] [planner_server-3]: process has finished cleanly [pid 661]


## validation/autonomy-20261006/results.json

{
  "date": "2026-10-06",
  "scope": "Ubuntu vacuum simulator only",
  "tests": {
    "free_space_goal": {
      "status": 4,
      "error_code": 0
    },
    "goal_beyond_wall": {
      "status": 6,
      "movement_m": 0.002205473557006596
    },
    "isolated_guard": {
      "clear_m_s": 0.2,
      "slow_m_s": 0.08000000000000002,
      "stop_m_s": 0.0,
      "scan_timeout_m_s": 0.0
    }
  },
  "passed": true
}


## validation/autonomy-20261006/isolated_guard.log

[INFO] [1791218153.261503466] [autonomy_guard_test.collision_monitor]: 
	collision_monitor lifecycle node launched. 
	Waiting on external lifecycle transitions to activate
	See https://design.ros2.org/articles/node_lifecycle.html for more information.
[INFO] [1791218153.669908906] [autonomy_guard_test.collision_monitor]: Configuring
[INFO] [1791218153.690206255] [collision_monitor]: [scan]: Creating Scan
[INFO] [1791218153.696715478] [collision_monitor]: [StopZone]: Creating Polygon
[INFO] [1791218153.702243347] [collision_monitor]: [SlowZone]: Creating Polygon
[INFO] [1791218153.754463026] [autonomy_guard_test.collision_monitor]: Activating
[INFO] [1791218153.754655862] [autonomy_guard_test.collision_monitor]: Creating bond (collision_monitor) to lifecycle manager.
[WARN] [1791218153.792823983] [autonomy_guard_test.collision_monitor]: Robot to stop due to invalid source. Either due to data not published yet, or to lack of new data received within the sensor timeout, or if impossible to transform data to base frame
[INFO] [1791218153.853243716] [autonomy_guard_test.collision_monitor]: Robot to continue normal operation
[INFO] [1791218155.365476670] [autonomy_guard_test.collision_monitor]: Robot to slowdown for 40.000000 percents due to SlowZone polygon
[INFO] [1791218156.881052786] [autonomy_guard_test.collision_monitor]: Robot to stop due to StopZone polygon
[INFO] [1791218158.402719323] [autonomy_guard_test.collision_monitor]: Robot to continue normal operation
[WARN] [1791218160.316880767] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.532000 seconds. Ignoring the source.
[WARN] [1791218160.316934060] [autonomy_guard_test.collision_monitor]: Robot to stop due to invalid source. Either due to data not published yet, or to lack of new data received within the sensor timeout, or if impossible to transform data to base frame
[WARN] [1791218160.368665193] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.584000 seconds. Ignoring the source.
[WARN] [1791218160.420295057] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.636000 seconds. Ignoring the source.
[WARN] [1791218160.473047762] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.688000 seconds. Ignoring the source.
[WARN] [1791218160.524829290] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.740000 seconds. Ignoring the source.
[WARN] [1791218160.576634633] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.792000 seconds. Ignoring the source.
[WARN] [1791218160.626893439] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.842000 seconds. Ignoring the source.
[WARN] [1791218160.679654476] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.894000 seconds. Ignoring the source.
[WARN] [1791218160.730702912] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.946000 seconds. Ignoring the source.
[WARN] [1791218160.781266403] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 0.996000 seconds. Ignoring the source.
[WARN] [1791218160.832456640] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.046000 seconds. Ignoring the source.
[WARN] [1791218160.883418305] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.098000 seconds. Ignoring the source.
[WARN] [1791218160.934804267] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.150000 seconds. Ignoring the source.
[WARN] [1791218160.988603151] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.202000 seconds. Ignoring the source.
[WARN] [1791218161.040853364] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.256000 seconds. Ignoring the source.
[WARN] [1791218161.091277028] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.306000 seconds. Ignoring the source.
[WARN] [1791218161.142395044] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.358000 seconds. Ignoring the source.
[WARN] [1791218161.193683701] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.408000 seconds. Ignoring the source.
[WARN] [1791218161.244690297] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.460000 seconds. Ignoring the source.
[WARN] [1791218161.297141976] [collision_monitor]: [scan]: Latest source and current collision monitor node timestamps differ on 1.512000 seconds. Ignoring the source.
[INFO] [1791218161.341375540] [rclcpp]: signal_handler(SIGINT/SIGTERM)
[INFO] [1791218161.341550218] [autonomy_guard_test.collision_monitor]: Running Nav2 LifecycleNode rcl preshutdown (collision_monitor)
[INFO] [1791218161.341667498] [autonomy_guard_test.collision_monitor]: Deactivating
[INFO] [1791218161.341699219] [autonomy_guard_test.collision_monitor]: Destroying bond (collision_monitor) to lifecycle manager.
[INFO] [1791218161.352941378] [autonomy_guard_test.collision_monitor]: Cleaning up
[INFO] [1791218161.353014819] [collision_monitor]: [StopZone]: Destroying Polygon
[INFO] [1791218161.353021255] [collision_monitor]: [SlowZone]: Destroying Polygon
[INFO] [1791218161.353025778] [collision_monitor]: [scan]: Destroying Scan
[INFO] [1791218161.363920866] [autonomy_guard_test.collision_monitor]: Destroying bond (collision_monitor) to lifecycle manager.
[INFO] [1791218161.406383323] [autonomy_guard_test.collision_monitor]: Destroying


## env.sh

#!/usr/bin/env bash
# Source from each development terminal. Intended exclusively for local simulation.
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
export ROS_DOMAIN_ID=42
export GZ_PARTITION=vacuum_sim_42
export GZ_IP=127.0.0.1
# Verified WSLg hardware rendering on this PC. Applies only to this workspace.
export GALLIUM_DRIVER=d3d12
export MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA
source /opt/ros/jazzy/setup.bash
vacuum_workspace="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$vacuum_workspace/install/setup.bash" ]]; then
  source "$vacuum_workspace/install/setup.bash"
fi
unset vacuum_workspace


## README.md

# Robot workspace



Open **Vacuum Lab.exe** and follow **Vacuum-Lab-Quickstart.md**. Click **Drive now**, center the yoke and arm once. You can drive without holding a button; center the yoke to stop.



The model has two under-chassis NEMA 17 motors, two TB6600 modules, 7 cm wheels, Arduino Mega 2560, Orange Pi 5 and RPLIDAR C1. Read **Hardware-Profile.md** for specifications and provisional geometry. Manual simulator limits are 1.5 m/s forward, 0.9 m/s reverse and 2.4 rad/s turning. The furnished world is 16 × 12 m.



**All project files** finds source, models/world/configuration, maps, logs and backups. The Linux workspace is `/home/robot/vacuum_ws` in WSL distro `VacuumRobot-24.04`. **Open robot code** connects VS Code to it. Use the launcher for driving, mapping/navigation, map saving and shutdown. Legacy keyboard teleop publishes directly and should not run alongside the launcher's controller.



Historical setup reports are retained with their dates. **modern-drive-validation.json** covers current motion and response; **directional-guard-validation.json** covers the guard; **executable-verification.json** covers the packaged launcher and file browser.



## Hardware-Profile.md

# Your vacuum robot

The Gazebo model now represents two NEMA 17 motors mounted below two acrylic chassis plates, one 7 cm diameter wheel on each motor, two TB6600 modules, an Arduino Mega 2560, an Orange Pi 5, an RPLIDAR C1, and the existing front camera. The wheel radius is 0.035 m in both the robot geometry and differential-drive controller. The lower chassis plate sits above the wheels and motor bodies; brackets connect the motors beneath it.

The 30 cm chassis diameter and 22 cm wheel separation are retained from the previous model. Motor body length, driver enclosure size, brackets, mass, and electronics positions are provisional because the exact NEMA 17 and TB6600 variants and your mechanical measurements were not supplied. These visual components do not implement physical stepper electronics or measure torque, missed steps, battery sag, or real motor temperature.

The simulated control path is yoke → Windows controller panel → ROS command gate → Collision Monitor → Gazebo differential-drive controller. Your intended physical architecture is Orange Pi 5 running ROS 2, Arduino Mega producing step/direction signals, and one TB6600 driving each NEMA 17. No firmware or physical motor commands are sent by this launcher.

Manual simulator limits are **1.5 m/s forward**, **0.9 m/s reverse**, and **2.4 rad/s turning**. Input and command forwarding run at 50 Hz. The dead zone starts at 5%, acceleration is 6 m/s², and odometry averaging uses three samples at 60 Hz. Arm once to drive with the yoke; center it to stop. **Require drive button** is an optional setting that starts off. STOP, disconnect, stale commands, and lidar/obstacle protection remain active. Autonomous navigation retains its existing 0.20 m/s planner limit.

At 1.5 m/s, direct-drive 70 mm wheels turn at approximately 409 RPM. This is a simulator setting, not a verified loaded speed for your particular NEMA 17/TB6600 setup.

The C1 sensor approximation uses 10 Hz scans, 500 samples per revolution, and a 0.05–12 m range. Its hardware profile records the 460800-baud UART interface. These values follow [SLAMTEC's C1 specifications](https://www.slamtec.com/en/c1/spec); Gazebo approximates its returns and does not reproduce reflectivity-dependent limits. The Arduino board outline uses the published dimensions in [Arduino's Mega 2560 product information](https://store-usa.arduino.cc/products/arduino-mega-2560-rev3).

The room is now **16 × 12 m**, with living, dining, kitchen, reading and home-office areas. The world uses a shared static body with batched materials to retain camera performance. Changes have a rollback archive in `~/vacuum_ws/model-backups/modern-hardware-20261007/before.tar.gz`.

The editable profile is `robot-profile.json`; the live ROS model is `src/vacuum_sim/urdf/vacuum.urdf.xacro`, its wheel/speed configuration is `config/controllers.yaml`, and the room generator is `tools/build_furnished_room.py`. Find these through **All project files**. Scene or robot changes need a simulation restart.

See **Robot-model-preview.png** for the assembled model and **Furnished-room-preview.png** for the room. Current drive, obstacle, navigation/map-save and executable reports are included beside this guide. Simulator shutdown now waits for its owned Gazebo child processes before releasing the single-simulator lock; startup checks use fresh ROS discovery.
