USE [master]
GO
/****** Object:  Login [user]    Script Date: 07.10.2020 8:36:07 ******/
DROP LOGIN [user]
GO

/* For security reasons the login is created disabled and with a random password. */
/****** Object:  Login [user]    Script Date: 07.10.2020 8:36:07 ******/
CREATE LOGIN [user] WITH PASSWORD=N'pass', DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[русский], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
ALTER LOGIN [user] ENABLE
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [user]
GO


