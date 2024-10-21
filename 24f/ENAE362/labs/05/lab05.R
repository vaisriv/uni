library(ggplot2)
library(gridExtra)
library(grid)

E_in <- c(
  0.0,
  0.102,
  0.196,
  0.301,
  0.397,
  0.497,
  0.603,
  0.705,
  0.796
)

E_out <- c(
  0.0,
  0.415,
  0.843,
  1.318,
  1.749,
  2.193,
  2.655,
  3.009,
  3.190
)

data <- data.frame(E_in = E_in, E_out = E_out)

p1 <- ggplot(data, aes(x = E_in, y = E_out)) +
  geom_point(shape = 21, fill = "white") +
  geom_line() +
  xlab(expression(E["in"] ~ "[V]")) +
  ylab(expression(E["out"] ~ "[V]")) +
  theme_bw(base_family = "serif") +
  theme(
    text = element_text(family = "serif"),
    panel.grid.major = element_blank(),
    panel.grid.minor = element_blank()
  )

title <- textGrob(
  expression("Figure 1: - Common Emitter Amplifier:" ~ E["out"] ~ "[V] versus" ~ E["in"] ~ "[V]"),
  gp = gpar(fontsize = 14, fontfamily = "serif"),
  hjust = 0.5
)

p1_out <- grid.arrange(p1, title, ncol = 1, heights = c(10, 1))

ggsave(filename = "E_in vs E_out plot.png", plot = p1_out, width = 6, height = 10)
