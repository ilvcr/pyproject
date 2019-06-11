/*
 Navicat Premium Data Transfer

 Source Server         : 192.168.145.128
 Source Server Type    : MySQL
 Source Server Version : 50725
 Source Host           : 192.168.145.128:3306
 Source Schema         : AnsbOps

 Target Server Type    : MySQL
 Target Server Version : 50725
 File Encoding         : 65001

 Date: 13/03/2019 16:32:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for rbac_permssions
-- ----------------------------
DROP TABLE IF EXISTS `rbac_permssions`;
CREATE TABLE `rbac_permssions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `perms` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `perms_img` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `perms_method` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `perms_id` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `perms_type` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `perms_url` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `parent_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `rbac_permssions_parent_id_cfda1317_fk_rbac_permssions_id`(`parent_id`) USING BTREE,
  CONSTRAINT `rbac_permssions_parent_id_cfda1317_fk_rbac_permssions_id` FOREIGN KEY (`parent_id`) REFERENCES `rbac_permssions` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rbac_permssions
-- ----------------------------
INSERT INTO `rbac_permssions` VALUES (1, '数据中心', 'fa-dashboard', 'GET', '05d6faf9-e05d-3454-b66e-57afdae1b3c0', '一级菜单', '正常', '', NULL);
INSERT INTO `rbac_permssions` VALUES (4, '资产仪表', 'fa-angle-right', 'GET', 'bd82e99f-9789-3cdb-bc7e-b31b055a68ef', '二级菜单', '正常', '/dashboard/', 1);
INSERT INTO `rbac_permssions` VALUES (6, '资产管理', 'fa-table', 'GET', '05d6faf9-e05d-3454-b66e-57afdae1b3c0', '一级菜单', '正常', '', NULL);
INSERT INTO `rbac_permssions` VALUES (8, '资产', 'fa-angle-right', 'GET', '3337c407-aaed-3334-abfd-5ba9d6e1426d', '二级菜单', '正常', '/cmdb/asset/', 6);
INSERT INTO `rbac_permssions` VALUES (9, '分组', 'fa-angle-right', 'GET', '294e6b18-7174-37c6-93fe-67907ec0acfb', '二级菜单', '正常', '/cmdb/group/', 6);
INSERT INTO `rbac_permssions` VALUES (10, '机房', 'fa-angle-right', 'GET', '2090a38d-0828-33a5-8119-c7851a7cdb7e', '二级菜单', '正常', '/cmdb/idc/', 6);
INSERT INTO `rbac_permssions` VALUES (11, '厂商', 'fa-angle-right', 'GET', '57a85652-b74e-301a-b38c-25ddc6b700e4', '二级菜单', '正常', '/cmdb/changshang/', 6);
INSERT INTO `rbac_permssions` VALUES (12, '系统管理', 'fa-th', 'GET', '05d6faf9-e05d-3454-b66e-57afdae1b3c0', '一级菜单', '正常', '', NULL);
INSERT INTO `rbac_permssions` VALUES (13, '用户管理', 'fa-angle-right', 'GET', '928e5d02-b7de-3382-8447-1343e74ff555', '二级菜单', '正常', '/rbac/user/', 12);
INSERT INTO `rbac_permssions` VALUES (14, '角色管理', 'fa-angle-right', 'GET', '44310348-af91-31ed-b627-bf498f394e2c', '二级菜单', '正常', '/rbac/role/', 12);
INSERT INTO `rbac_permssions` VALUES (15, '权限管理', 'fa-angle-right', 'GET', '25bc3407-6a55-3ec0-bdff-9296d5aea72a', '二级菜单', '正常', '/rbac/perms/', 12);
INSERT INTO `rbac_permssions` VALUES (16, '添加', '', 'POST', 'dc1e97f3-3876-32d3-8e57-b273ec9e0a0a', '功能权限', '正常', '/cmdb/group/', 9);
INSERT INTO `rbac_permssions` VALUES (17, '修改', '', 'PUT', '4f1746bd-4dc0-31b5-bc83-7b0a0d4a1c49', '功能权限', '正常', '/cmdb/group/', 9);
INSERT INTO `rbac_permssions` VALUES (18, '删除', '', 'GET', '294e6b18-7174-37c6-93fe-67907ec0acfb', '功能权限', '正常', '/cmdb/group/', 9);
INSERT INTO `rbac_permssions` VALUES (19, '添加', '', 'POST', '606c7dfc-6cc2-3919-90c8-dbf8a2eb85a6', '功能权限', '正常', '/rbac/user/', 13);
INSERT INTO `rbac_permssions` VALUES (20, '修改', '', 'PUT', '5d2de6e8-8527-33d7-b175-21f537a40659', '功能权限', '正常', '/rbac/user/', 13);

SET FOREIGN_KEY_CHECKS = 1;
