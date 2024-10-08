library(ggplot2)
library(gridExtra)
library(grid)

E_measured <- c(
  0.0,
  0.102,
  0.301,
  0.602,
  1.201,
  2.004,
  3.024,
  4.105,
  5.018,
  6.240,
  7.045,
  7.914,
  10.078,
  12.010,
  14.070,
  16.027
)

R_measured <- 100.1

I_F <- E_measured / R_measured * 1000 # ma

E_F <- c(
  0.0,
  0.6,
  0.65,
  0.68,
  0.71,
  0.73,
  0.75,
  0.76,
  0.77,
  0.78,
  0.78,
  0.78,
  0.79,
  0.80,
  0.80,
  0.80
)

data <- data.frame(E_F = E_F, I_F = I_F)

p <- ggplot(data, aes(x = E_F, y = I_F)) +
  geom_point(shape = 21, fill = "white") +
  geom_line() +
  xlab(expression(E[F] ~ "[V]")) +
  ylab(expression(I[F] ~ "[mA]")) +
  theme_bw(base_family = "serif") +
  theme(
    text = element_text(family = "serif"),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank()
  )

title <- textGrob(
  expression(I[F] ~ "[mA] versus" ~ E[F] ~ "[V]"),
  gp = gpar(fontsize = 14, fontfamily = "serif"),
  hjust = 0.5
)

grid.arrange(p, title, ncol = 1, heights = c(10, 1))

E_R <- -1*c(
  0,
  0.007,
  0.012,
  0.146,
  0.904,
  1.820,
  2.831,
  4.709,
  6.842,
  8.877,
  10.603
)

I_Z <- E_R / R_measured * 1000

E_Z <- -1*c(
  0,
  1.972,
  3.96,
  4.82,
  5.11,
  5.16,
  5.20,
  5.24,
  5.30,
  5.33,
  5.37
)

data2 <- data.frame(E_Z = E_Z, I_Z = I_Z)

p2 <- ggplot(data2, aes(x = E_Z, y = I_Z)) +
  geom_point(shape = 21, fill = "white") +
  geom_line() +
  xlab(expression(E[Z] ~ "[V]")) +
  ylab(expression(I[Z] ~ "[mA]")) +
  theme_bw(base_family = "serif") +
  theme(
    text = element_text(family = "serif"),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank()
  ) +
  scale_x_continuous(position = "top") +
  scale_y_continuous(position = "right")

title2 <- textGrob(
  expression(I[Z] ~ "[mA] versus" ~ E[Z] ~ "[V]"),
  gp = gpar(fontsize = 14, fontfamily = "serif"),
  hjust = 0.5
)

grid.arrange(p2, title2, ncol = 1, heights = c(10, 1))
