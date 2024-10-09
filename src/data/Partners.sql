-- Volcando estructura para tabla esf.Partners
DROP TABLE IF EXISTS `Partners`;
CREATE TABLE IF NOT EXISTS `Partners` (
  `PartnerId` int(11) NOT NULL AUTO_INCREMENT,
  `ContactId` bigint(20) NOT NULL,
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`PartnerId`),
  KEY `FK_Partners_ContactId` (`ContactId`),
  CONSTRAINT `FK_Partners_ContactId` FOREIGN KEY (`ContactId`) REFERENCES `Contacts` (`ContactId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
