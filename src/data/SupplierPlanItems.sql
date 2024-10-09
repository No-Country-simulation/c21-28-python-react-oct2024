DROP TABLE IF EXISTS `SupplierPlanItems`;
CREATE TABLE IF NOT EXISTS `SupplierPlanItems` (
  `SupplierPlanItemId` int(11) NOT NULL AUTO_INCREMENT,
  `SupplierPlanId` int(11) NOT NULL,
  `SupplierItemId` int(11) NOT NULL,
  `Description` varchar(100) CHARACTER SET utf8 NOT NULL,
  `Order` smallint(6) NOT NULL DEFAULT '0',
  `PercentageCovered` decimal(4,2) NOT NULL DEFAULT '0.00',
  `AmountCovered` decimal(18,2) NOT NULL DEFAULT '0.00',
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`SupplierPlanItemId`),
  UNIQUE KEY `UQ_SupplierPlanItems` (`SupplierPlanId`,`SupplierItemId`),
  KEY `FK_SupplierPlanItems_SupplierItemId` (`SupplierItemId`),
  CONSTRAINT `FK_SupplierPlanItems_SupplierPlanId` FOREIGN KEY (`SupplierPlanId`) REFERENCES `SupplierPlans` (`SupplierPlanId`),
  CONSTRAINT `FK_SupplierPlanItems_SupplierItemId` FOREIGN KEY (`SupplierItemId`) REFERENCES `SupplierItems` (`SupplierItemId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
