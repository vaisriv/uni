library(ggplot2)
library(gridExtra)
library(grid)

R_act <- c(
  0.1,
  0.93,
  1.72,
  2.45,
  3.34,
  4.13,
  4.92,
  5.75,
  6.53,
  7.31,
  8.14,
  8.92,
  9.37
)

Pulses <- c(
  0,
  10,
  20,
  30,
  40,
  50,
  60,
  70,
  80,
  90,
  100,
  110,
  120
)

data <- data.frame(R_act = R_act, Pulses = Pulses)

p1 <- ggplot(data, aes(x = R_act, y = Pulses)) +
  geom_point(shape = 21, fill = "white") +
  geom_line() +
  xlab(expression(R["actual"] ~ "[KOhms]")) +
  ylab(expression("Pulses")) +
  theme_bw(base_family = "serif") +
  theme(
    text = element_text(family = "serif"),
  )

title <- textGrob(
  expression("Figure 1: - Digital Plot: Pulses versus" ~ R["actual"] ~ "[KOhms]"),
  gp = gpar(fontsize = 14, fontfamily = "serif"),
  hjust = 0.5
)

p1_out <- grid.arrange(p1, title, ncol = 1, heights = c(10, 1))

ggsave(filename = "Pulses vs R_actual plot.png", plot = p1_out, width = 8.5, height = 11)
