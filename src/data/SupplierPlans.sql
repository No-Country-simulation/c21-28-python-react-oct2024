DROP TABLE IF EXISTS `SupplierPlans`;
CREATE TABLE IF NOT EXISTS `SupplierPlans` (
  `SupplierPlanId` int(11) NOT NULL AUTO_INCREMENT,
  `SupplierId` int(11) NOT NULL,
  `Description` varchar(100) CHARACTER SET utf8 NOT NULL,
  `Order` smallint(6) NOT NULL DEFAULT '0',
  `IsDefault` tinyint(1) NOT NULL DEFAULT '0',
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`SupplierPlanId`),
  KEY `FK_SupplierPlans_SupplierId` (`SupplierId`),
  CONSTRAINT `FK_SupplierPlans_SupplierId` FOREIGN KEY (`SupplierId`) REFERENCES `Suppliers` (`SupplierId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
