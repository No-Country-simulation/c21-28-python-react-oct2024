DROP TABLE IF EXISTS `Notes`;
CREATE TABLE IF NOT EXISTS `Notes` (
  `NoteId` int(11) NOT NULL AUTO_INCREMENT,
  `CompanyId` int(11) NOT NULL,
  `EntityType` varchar(100) CHARACTER SET utf8 DEFAULT NULL,
  `RowId` bigint(20) NOT NULL,
  `Text` varchar(2000) CHARACTER SET utf8 NOT NULL,
  `IsActive` smallint(6) NOT NULL DEFAULT '1',
  `CreatedAt` datetime NOT NULL,
  `UpdatedAt` datetime DEFAULT NULL,
  `DeletedAt` datetime DEFAULT NULL,
  `CreatedBy` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UpdatedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `DeletedBy` varchar(50) CHARACTER SET utf8 DEFAULT NULL,
  `Title` varchar(100) CHARACTER SET utf8 NOT NULL,
  PRIMARY KEY (`NoteId`),
  KEY `FK_Notes_CompanyId` (`CompanyId`),
  KEY `FK_Notes_NoteTypeId` (`NoteTypeId`),
  CONSTRAINT `FK_Notes_CompanyId` FOREIGN KEY (`CompanyId`) REFERENCES `Companies` (`CompanyId`),
  CONSTRAINT `FK_Notes_NoteTypeId` FOREIGN KEY (`NoteTypeId`) REFERENCES `NoteTypes` (`NoteTypeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
