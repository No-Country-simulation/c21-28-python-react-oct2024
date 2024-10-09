DROP TABLE IF EXISTS `SupplierItems`;
CREATE TABLE IF NOT EXISTS `SupplierItems` (
  `SupplierItemId` int(11) NOT NULL AUTO_INCREMENT,
  `SupplierId` int(11) NOT NULL,
  `ItemId` int(11) NOT NULL,
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`SupplierItemId`),
  UNIQUE KEY `UQ_SupplierItems` (`SupplierId`,`ItemId`),
  KEY `FK_SupplierItems_ItemId` (`ItemId`),
  CONSTRAINT `FK_SupplierItems_ItemId` FOREIGN KEY (`ItemId`) REFERENCES `Items` (`ItemId`),
  CONSTRAINT `FK_SupplierItems_SupplierId` FOREIGN KEY (`SupplierId`) REFERENCES `Suppliers` (`SupplierId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
